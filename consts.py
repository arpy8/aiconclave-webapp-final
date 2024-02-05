lions = """01001001 01101110 00100000 01110100 01101000 01100101 00100000 01110111 01101001 01101100 01100100 00101100 00100000 01001001 00100111 01101101 00100000 01101011 01101110 01101111 01110111 01101110 00100000 01100001 01110011 00100000 01110100 01101000 01100101 00100000 01101011 01101001 01101110 01100111 00101100 00001010 01010111 01101001 01110100 01101000 00100000 01100001 00100000 01101101 01100001 01101010 01100101 01110011 01110100 01101001 01100011 00100000 01101101 01100001 01101110 01100101 00101100 00100000 01001001 00100000 01110000 01110010 01101111 01110101 01100100 01101100 01111001 00100000 01100010 01110010 01101001 01101110 01100111 00101110 00001010 01010011 01111001 01101101 01100010 01101111 01101100 00100000 01101111 01100110 00100000 01100011 01101111 01110101 01110010 01100001 01100111 01100101 00101100 00100000 01110011 01110100 01110010 01100101 01101110 01100111 01110100 01101000 00101100 00100000 01100001 01101110 01100100 00100000 01101101 01101001 01100111 01101000 01110100 00101100 00001010 01010111 01101000 01100001 01110100 00100000 01100001 01101101 00100000 01001001 00100000 01100011 01100001 01101100 01101100 01100101 01100100 00111111 00001010 00001010 01000011 01101111 01100100 01100101 00111010 00100000 01000001 01001001 01000011 00110010 00111001 00110111"""
parking = """D ydvw duhd iru yhklfohv, odujh ru vpdoo, Zkhuh fduv dqg wuxfnv, wkhb vwdqg lq d vsudzo. Irxqg qhdu exloglqjv, d frqyhqlhqw vsrw, Zkdw dp L fdoohg?"""

final_question = ".. ....... ... - .- -. -.. ....... .. -. ....... - .... . ....... ..- -. .. ...- . .-. ... .. - -.-- --..-- ....... - .-. .- -. ... .--. .- .-. . -. - ....... .- -. -.. ....... - .- .-.. .-.. --..-- .-. . ..-. .-.. . -.-. - .. -. --. ....... ... ..- .-. .-. --- ..- -. -.. .. -. --. ... --..-- ....... .- ....... --. .-.. . .- -- .. -. --. ....... ... .--. .-. .- .-- .-.. .-.-.- .-- .. - .... ....... .-- .- .-.. .-.. ... ....... --- ..-. ....... --. .-.. .- ... ... ....... .- -. -.. ....... ... .... .. -- -- . .-. .. -. --. ....... ... .. --. .... - --..-- ....... ..-. .. -. -.. ....... -- . --..-- .-- .... . .-. . ....... .- -- ....... .. ..--.."

data_dict = {
    "binary": [{"problem_top":"You stumble upon a mysterious message written in binary code:", 
                "problem_bottom": "Can you decipher this message to reveal what it says? Once decoded, identify the significance of the message in the context of computer science.",
                "problem_hint": "Binary code often represents characters using ASCII encoding. Each group of 8 bits (1 byte) corresponds to a character. You can use an ASCII table to decode the binary message."}
    ],
    "caesar": [{"problem_top":"You find a message written in a strange language:",
               "problem_statement": "D ydvw duhd iru yhklfohv, odujh ru vpdoo, Zkhuh fduv dqg wuxfnv, wkhb vwdqg lq d vsudzo. Irxqg qhdu exloglqjv, d frqyhqlhqw vsrw, Zkdw dp L fdoohg?",
               "problem_bottom": "Can you decipher this message to reveal what it says? Once decoded, identify the significance of the message in the context of computer science.",
                "problem_hint": "The message is encrypted using a Caesar cipher. You can decrypt the message by shifting each letter by a fixed number of positions down the alphabet. The number of positions is the key to the cipher."}
    ],
}

