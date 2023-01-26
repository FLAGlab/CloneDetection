import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);
  // This widget is the root of your application
  @override
  Widget build(BuildContext context) {
    String s;
    s='Hello Flutter';
    return MaterialApp(
      title: 'Flutter Demo', //app name
      home: Scaffold(
          appBar: AppBar(title: const Text('Welcome to flutter'),),
          body: Center(child: Text('Hello Flutter'),)
      ),
    );
  }
}
