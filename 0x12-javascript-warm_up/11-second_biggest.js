#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  let stp;
  let bucket = [];
  for (stp = 2; stp < process.argv.length; stp++) {
    bucket.push(parseInt(process.argv[stp]));
  }
  bucket = bucket.sort(function (x, y) {
    return x - y;
  });
  console.log(bucket[bucket.length - 2]);
}
