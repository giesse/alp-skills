# Invoice totals

An invoice should make every charged amount understandable to the customer.
Prices are displayed in the invoice currency with two decimal places.

## Discounts and tax

An order-level percentage discount is applied before tax. Tax is computed for
each line, rounded to the nearest cent, and then added to the discounted
subtotal.

To prevent intermediate rounding from changing the total, the calculation
keeps exact decimal amounts across all lines, sums them, and rounds tax only
once for the invoice.

For example, two taxable lines of 0.05 each at a ten-percent tax rate produce
0.01 total tax.

## Refunds

A full refund returns the amount originally paid. A partial refund returns the
selected lines and their associated tax. When an order-level discount was
used, the refund includes the relevant part of that discount.

Imported catalog prices are accepted from partner systems and displayed with
two decimal places.
