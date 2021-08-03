# JStoTSenum
Coded this as a tool to speed up Typing of [DoctorMcKay/node-steam-user](https://github.com/DoctorMcKay/node-steam-user)
This converter takes JavaScript Enums like [these](https://github.com/DoctorMcKay/node-steam-user/tree/master/enums):
```js
module.exports = {
    "NoCost": 0,
    "BillOnceOnly": 1,
    "BillMonthly": 2,
    "ProofOfPrepurchaseOnly": 3,
    "GuestPass": 4,
    "HardwarePromo": 5,
    "Gift": 6,
}
```

and converts them to TypeScript Enums like this:
```ts
export enum EBillingType {
    "NoCost" = 0;
    "BillOnceOnly" = 1;
    "BillMonthly" = 2;
    "ProofOfPrepurchaseOnly" = 3;
    "GuestPass" = 4;
    "HardwarePromo" = 5;
    "Gift" = 6;
}
```

Enum naming is based on the JavaScript Filenames, so there can only be one Enum per JavaScript file.
The converter takes a directory full of JavaScript files as input, and the output directory can be configured.
