import 'package:crypto_client/providers/auth.dart';
import 'package:crypto_client/providers/investments.dart';
import 'package:crypto_client/screns/investments_screen.dart';
import 'package:crypto_client/screns/login_screen.dart';
import 'package:crypto_client/screns/register_screen.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

void main() {
  runApp(MultiProvider(providers: [
    ChangeNotifierProvider(
      create: (context) => AuthProvider(),
    ),
    ChangeNotifierProxyProvider<AuthProvider, InvestmentsProvider>(
      create: (context) => InvestmentsProvider(),
      update: (context, auth, folders) => folders!..updateAuth(auth.token),
    ),
  ], child: const MyApp()));
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: LoginScreen(),
      routes: {
        '/login': (context) => LoginScreen(),
        '/register': (context) => RegisterScreen(),
        '/investments': (context) => InvestmentsScreen(),
      },
    );
  }
}
