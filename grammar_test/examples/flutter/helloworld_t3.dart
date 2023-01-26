import 'package:flutter/material.dart';
import 'dart:math';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    String s;
    if(Random().nextInt(10) % 2 == 0) {
      s = 'Hello Odd Flutter';
    } else {
      s = 'Hello Even Flutter';
    }
    return MaterialApp(
      title: 'Flutter Demo',
      home: Scaffold(
          appBar: AppBar( title: const Text('Welcome to flutter'),),
          body: Center(child: Text(s),)
      ),
    );
  }
}
