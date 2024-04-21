import { faker } from '@faker-js/faker';

interface Transaction {
  id: string;
  date: Date;
  amount: number;
  description: string;
  category: string;
}

export function generateTransactions(): Transaction[] {
  const transactions: Transaction[] = [];
  const startDate = new Date();
  startDate.setFullYear(startDate.getFullYear() - 1); // Set start date to one year ago

  for (let i = 0; i < 31; i++) {
    // Generate data for each day of the year
    const transactionCount = faker.datatype.number({ min: 1, max: 10 }); // Random number of transactions per day
    for (let j = 0; j < transactionCount; j++) {
      transactions.push({
        id: faker.datatype.uuid(),
        date: new Date(startDate),
        amount: parseFloat(faker.finance.amount(10, 1000, 2)),
        description: faker.finance.transactionDescription(),
        category: faker.helpers.arrayElement(['Groceries', 'Entertainment', 'Utilities', 'Rent', 'Miscellaneous']),
      });
    }
    startDate.setDate(startDate.getDate() + 1); // Increment the date
  }
  return transactions;
}
