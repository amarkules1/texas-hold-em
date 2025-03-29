declare module 'dataframe-js' {
    export class DataFrame {
        constructor(data: string | any[]);
        
        filter(predicate: (row: Row) => boolean): DataFrame;
        count(): number;
        toCollection(): any[];
    }

    export interface Row {
        get(columnName: string): any;
        [key: string]: any;
    }
}
