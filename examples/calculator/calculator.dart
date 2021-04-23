import 'package:flutter/material.dart';

class Numbers extends StatefulWidget {
  @override
  _NumbersState createState() => _NumbersState();
}

class _NumbersState extends State<Numbers> {
  String output = "0";

  String _output = "0";
  double number1 = 0.0;
  double number2 = 0.0;
  String operand = "";

  buttonPressed(String buttonNumber) {
    if (buttonNumber == "CLEAR") {
      _output = "0";
      number1 = 0.0;
      number2 = 0.0;
      operand = "";
    } else if (buttonNumber == "+" ||
        buttonNumber == "-" ||
        buttonNumber == "/" ||
        buttonNumber == "X") {
      number1 = double.parse(output);
      operand = buttonNumber;
      _output = "0";
    } else if (buttonNumber == ".") {
      if (_output.contains(".")) {
        return;
      } else {
        _output = _output + buttonNumber;
      }
    } else if (buttonNumber == "=") {
      number2 = double.parse(output);
      if (operand == "+") {
        _output = (number1 + number2).toString();
      }
      if (operand == "-") {
        _output = (number1 - number2).toString();
      }
      if (operand == "X") {
        _output = (number1 * number2).toString();
      }
      if (operand == "/") {
        _output = (number1 / number2).toString();
      }
      number1 = 0.0;
      number2 = 0.0;
      operand = "";
    } else {
      _output = _output + buttonNumber;
    }
    setState(() {
      output = double.parse(_output).toStringAsFixed(2);
    });
  }

  Widget buildButton(String buttonNumber) {
    return Expanded(
      child: OutlineButton(
        padding: EdgeInsets.all(24),
        child: Text(
          buttonNumber,
          style: TextStyle(fontWeight: FontWeight.bold, fontSize: 20),
        ),
        onPressed: () {
          buttonPressed(buttonNumber);
        },
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Column(
        children: [
          Container(
              alignment: Alignment.centerRight,
              padding: EdgeInsets.symmetric(vertical: 24, horizontal: 12),
              child: Text(
                output,
                style: TextStyle(fontSize: 36, fontWeight: FontWeight.bold),
              )),
          Expanded(
            child: Divider(),
          ),
          Column(
            children: [
              Row(
                children: [
                  buildButton("7"),
                  buildButton("8"),
                  buildButton("9"),
                  buildButton("/"),
                ],
              ),
              Row(
                children: [
                  buildButton("4"),
                  buildButton("5"),
                  buildButton("6"),
                  buildButton("X"),
                ],
              ),
              Row(
                children: [
                  buildButton("1"),
                  buildButton("2"),
                  buildButton("3"),
                  buildButton("-"),
                ],
              ),
              Row(
                children: [
                  buildButton("."),
                  buildButton("0"),
                  buildButton("00"),
                  buildButton("+"),
                ],
              ),
              Row(
                children: [
                  buildButton("CLEAR"),
                  buildButton("="),
                ],
              ),
            ],
          ),
        ],
      ),
    );
  }
}