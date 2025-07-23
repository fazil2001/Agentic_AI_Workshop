def is_numeric(column):
    return column.dtype.kind in 'biufc'
