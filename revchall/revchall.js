var flag = atob("EhsAQW9bQCQBAAcACAoMGAw2FzoGETkNHBE+HwAmHhsU");
var xorkey = "this_is_xor_key";
var decoded = "";
for (var i=0; i<flag.length; i++) {
    decoded += String.fromCharCode(flag[i].charCodeAt() ^ xorkey[i % xorkey.length].charCodeAt());
}
console.log(decoded);
