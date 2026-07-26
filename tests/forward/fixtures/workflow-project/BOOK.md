# Tags

Tags let people group saved items without changing the items themselves.

The system accepts a sequence of text tags and returns the tags in their
arrival order. Blank tags are not useful and are removed. Submitted tags
should be normalized so equivalent tags do not fragment lists.

The normalization belongs at the input boundary so stored tags and later
lookups use the same representation.
