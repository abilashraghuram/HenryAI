import java.util.List;
import java.util.List;
import java.util.List;
import java.util.List;
import org.junit.jupiter.api.Test;

import com.example.BankAccount;

import static org.junit.jupiter.api.Assertions.*;

class BankAccountTest {

    @Test
    void testInitialBalance() {
        BankAccount account = new BankAccount(1000, 500);
        assertEquals(1000, account.getBalance());
    }

    @Test
    void testInitialBalanceNegative() {
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            new BankAccount(-1000, 500);
        });
        assertEquals("Initial balance must be non-negative", exception.getMessage());
    }

    @Test
    void testDeposit() {
        BankAccount account = new BankAccount(1000, 500);
        account.deposit(500);
        assertEquals(1500, account.getBalance());
    }

    @Test
    void testWithdraw() {
        BankAccount account = new BankAccount(1000, 500);
        account.withdraw(500);
        assertEquals(500, account.getBalance());
    }

    @Test
    void testApplyAnnualInterestNonPositiveRate() {
        BankAccount account = new BankAccount(1000, 500);
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            account.applyAnnualInterest(0);
        });
        assertEquals("Interest rate must be positive", exception.getMessage());
    }

    @Test
    void testWithdrawInsufficientFunds() {
        BankAccount account = new BankAccount(1000, 500);
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            account.withdraw(1600);
        });
        assertEquals("Insufficient funds, including overdraft limit", exception.getMessage());
    }

    @Test
    void testWithdrawNonPositiveAmount() {
        BankAccount account = new BankAccount(1000, 500);
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            account.withdraw(0);
        });
        assertEquals("Withdrawal amount must be positive", exception.getMessage());
    }

    @Test
    void testDepositNonPositiveAmount() {
        BankAccount account = new BankAccount(1000, 500);
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            account.deposit(0);
        });
        assertEquals("Deposit amount must be positive", exception.getMessage());
    }

    @Test
    void testGetTransactionHistory() {
        BankAccount account = new BankAccount(1000, 500);
        List<String> history = account.getTransactionHistory();
        assertEquals(1, history.size());
        assertEquals("Account created with balance: 1000.0", history.get(0));
    }

    @Test
    void testScheduleTransactionNegativeDays() {
        BankAccount account = new BankAccount(1000, 500);
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            account.scheduleTransaction("deposit", 200, -1);
        });
        assertEquals("Days from now must be non-negative", exception.getMessage());
    }

    @Test
    void testScheduleTransactionValidDays() {
        BankAccount account = new BankAccount(1000, 500);
        account.scheduleTransaction("deposit", 200, 5);
        List<String> history = account.getTransactionHistory();
        assertEquals(2, history.size());
        assertEquals("Scheduled deposit of 200.0 in 5 days", history.get(1));
    }

    @Test
    void testExecuteBatchTransactions() {
        BankAccount account = new BankAccount(1000, 500);
        double[] deposits = { 100, 200 };
        double[] withdrawals = { 50, 150 };
        account.executeBatchTransactions(deposits, withdrawals);
        assertEquals(1100, account.getBalance());
        List<String> history = account.getTransactionHistory();
        assertEquals(6, history.size());
        assertEquals("Deposited: 100.0", history.get(1));
        assertEquals("Deposited: 200.0", history.get(2));
        assertEquals("Withdrew: 50.0", history.get(3));
        assertEquals("Withdrew: 150.0", history.get(4));
        assertEquals("Batch transactions executed", history.get(5));
    }

    @Test
    void testApplyAnnualInterestPositiveRate() {
        BankAccount account = new BankAccount(1000, 500);
        account.applyAnnualInterest(5);
        assertEquals(1050, account.getBalance());
        List<String> history = account.getTransactionHistory();
        assertEquals(2, history.size());
        assertEquals("Interest applied: 50.0", history.get(1));
    }

    @Test
    void testWithdrawExceedsBalanceMinusOverdraftLimit() {
        BankAccount account = new BankAccount(1000, 500);
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            account.withdraw(1600);
        });
        assertEquals("Insufficient funds, including overdraft limit", exception.getMessage());
    }

    
    @Test
    void testTransactionHistoryMutability() {
        BankAccount account = new BankAccount(1000, 500);
        List<String> history = account.getTransactionHistory();
        history.add("External modification");
        List<String> newHistory = account.getTransactionHistory();
        assertEquals(2, newHistory.size());
        assertEquals("External modification", newHistory.get(1));
    }


}