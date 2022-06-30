// Decimals from WEI to 10 ** -8
const etherDecimals = new BN(10).pow(new BN(10));
// Decimals from GWEI to WEI
const gweiDecimals = new BN(10).pow(new BN(9));
const decimals = new BigNumber('100000000');
const zdecimals = new BN(10).pow(new BN(8));

var rbtcswapabi = [
    {
      anonymous: false,
      inputs: [
        {
          indexed: true,
          internalType: 'bytes32',
          name: 'preimageHash',
          type: 'bytes32',
        },
        {
          indexed: false,
          internalType: 'bytes32',
          name: 'preimage',
          type: 'bytes32',
        },
      ],
      name: 'Claim',
      type: 'event',
    },
    {
      anonymous: false,
      inputs: [
        {
          indexed: true,
          internalType: 'bytes32',
          name: 'preimageHash',
          type: 'bytes32',
        },
        {
          indexed: false,
          internalType: 'uint256',
          name: 'amount',
          type: 'uint256',
        },
        {
          indexed: false,
          internalType: 'address',
          name: 'claimAddress',
          type: 'address',
        },
        {
          indexed: true,
          internalType: 'address',
          name: 'refundAddress',
          type: 'address',
        },
        {
          indexed: false,
          internalType: 'uint256',
          name: 'timelock',
          type: 'uint256',
        },
      ],
      name: 'Lockup',
      type: 'event',
    },
    {
      anonymous: false,
      inputs: [
        {
          indexed: true,
          internalType: 'bytes32',
          name: 'preimageHash',
          type: 'bytes32',
        },
      ],
      name: 'Refund',
      type: 'event',
    },
    {
      inputs: [
        { internalType: 'bytes32', name: 'preimage', type: 'bytes32' },
        { internalType: 'uint256', name: 'amount', type: 'uint256' },
        { internalType: 'address', name: 'refundAddress', type: 'address' },
        { internalType: 'uint256', name: 'timelock', type: 'uint256' },
      ],
      name: 'claim',
      outputs: [],
      stateMutability: 'nonpayable',
      type: 'function',
    },
    {
      inputs: [
        { internalType: 'bytes32', name: 'preimageHash', type: 'bytes32' },
        { internalType: 'uint256', name: 'amount', type: 'uint256' },
        { internalType: 'address', name: 'claimAddress', type: 'address' },
        { internalType: 'address', name: 'refundAddress', type: 'address' },
        { internalType: 'uint256', name: 'timelock', type: 'uint256' },
      ],
      name: 'hashValues',
      outputs: [{ internalType: 'bytes32', name: '', type: 'bytes32' }],
      stateMutability: 'pure',
      type: 'function',
    },
    {
      inputs: [
        { internalType: 'bytes32', name: 'preimageHash', type: 'bytes32' },
        { internalType: 'address', name: 'claimAddress', type: 'address' },
        { internalType: 'uint256', name: 'timelock', type: 'uint256' },
      ],
      name: 'lock',
      outputs: [],
      stateMutability: 'payable',
      type: 'function',
    },
    {
      inputs: [
        { internalType: 'bytes32', name: 'preimageHash', type: 'bytes32' },
        {
          internalType: 'address payable',
          name: 'claimAddress',
          type: 'address',
        },
        { internalType: 'uint256', name: 'timelock', type: 'uint256' },
        { internalType: 'uint256', name: 'prepayAmount', type: 'uint256' },
      ],
      name: 'lockPrepayMinerfee',
      outputs: [],
      stateMutability: 'payable',
      type: 'function',
    },
    {
      inputs: [
        { internalType: 'bytes32', name: 'preimageHash', type: 'bytes32' },
        { internalType: 'uint256', name: 'amount', type: 'uint256' },
        { internalType: 'address', name: 'claimAddress', type: 'address' },
        { internalType: 'uint256', name: 'timelock', type: 'uint256' },
      ],
      name: 'refund',
      outputs: [],
      stateMutability: 'nonpayable',
      type: 'function',
    },
    {
      inputs: [{ internalType: 'bytes32', name: '', type: 'bytes32' }],
      name: 'swaps',
      outputs: [{ internalType: 'bool', name: '', type: 'bool' }],
      stateMutability: 'view',
      type: 'function',
    },
    {
      inputs: [],
      name: 'version',
      outputs: [{ internalType: 'uint8', name: '', type: 'uint8' }],
      stateMutability: 'view',
      type: 'function',
    },
  ];