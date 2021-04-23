import 'package:flutter/material.dart';

// This is a comment
class Numbers extends StatefulWidget {
  @override
  StateNumbers createState() => StateNumbers();
}

class StateNumbers extends State<Numbers> {
  // This is a comment
  String output = "0";

  String _out = "0";
  double num1 = 0.0;
  double num2 = 0.0;
  // This is a comment
  String operand = "";

  buttonPressed(String actButtonNum) {
    // This is a comment
    if (actButtonNum == "CLEAR") {
      _out = "0";
      num1 = 0.0;
      num2 = 0.0;
      operand = "";
    } else if (actButtonNum == "+" ||
        actButtonNum == "-" ||
        actButtonNum == "/" ||
        actButtonNum == "X") {
      num1 = double.parse(output);
      // This is a comment
      operand = actButtonNum;
      _out = "0";
    } else if (actButtonNum == ".") {
      if (_out.contains(".")) {
        return;
      } else {
        _out = _out + actButtonNum;
      }
    } else if (actButtonNum == "=") {
      num2 = double.parse(output);
      if (operand == "+") {
        _out = (num1 + num2).toString();
        // This is a comment
      }
      if (operand == "-") {
        _out = (num1 - num2).toString();
      }
      if (operand == "X") {
        _out = (num1 * num2).toString();
      }
      if (operand == "/") {
        _out = (num1 / num2).toString();
      }
      num1 = 0.0;
      num2 = 0.0;
      // This is a comment
      operand = "";
    } else {
      _out = _out + actButtonNum;
    }
    setState(() {
      output = double.parse(_out).toStringAsFixed(2);
      // This is a comment
    });
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

  Widget buildButton(String actButtonNum) {
    return Expanded(
      child: OutlineButton(
        padding: EdgeInsets.all(24),
        child: Text(
          actButtonNum,
          style: TextStyle(fontWeight: FontWeight.bold, fontSize: 20),
        ),
        onPressed: () {
          buttonPressed(actButtonNum);
        },
      ),
    );
  }
}