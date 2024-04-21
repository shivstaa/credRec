import type { NextApiRequest, NextApiResponse } from 'next';
import { generateTransactions } from '../../../fakedata'

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  const transactions = generateTransactions();
  res.status(200).json(transactions);
}
