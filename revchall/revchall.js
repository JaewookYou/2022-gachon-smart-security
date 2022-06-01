//var flag = "flag{this_is_reversing_chall_example_flag}";
var flag = atob("EgQIFCQdGzYLMBssNBccAg0bADYHFAAbBxMzBzocDAkEAzMMLDkUDhUi");
var xorkey = "this_is_xor_key";
var encoded = "";
for (var i=0; i<flag.length; i++) {
    encoded += String.fromCharCode(flag[i].charCodeAt() ^ xorkey[i % xorkey.length].charCodeAt());
}
console.log(encoded);
