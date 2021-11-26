import 'package:crypto_client/providers/investments.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'dart:math' as math;
import 'package:provider/provider.dart';

class InvestmentsScreen extends StatefulWidget {
  InvestmentsScreen({Key? key}) : super(key: key);

  @override
  _InvestmentsScreenState createState() => _InvestmentsScreenState();
}

class _InvestmentsScreenState extends State<InvestmentsScreen> {
  @override
  void initState() {
    Provider.of<InvestmentsProvider>(context, listen: false).fetchInvestments();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    final investments = Provider.of<InvestmentsProvider>(context).investments;

    return Scaffold(
      appBar: AppBar(
        title: const Text('Investments'),
        actions: <Widget>[
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: () {
              Navigator.pushReplacementNamed(context, '/login');
            },
          ),
        ],
      ),
      body: RefreshIndicator(
        onRefresh: () async {
          await Provider.of<InvestmentsProvider>(context, listen: false)
              .fetchInvestments();
        },
        child: ListView.builder(
          itemCount: investments.length,
          itemBuilder: (context, index) {
            return Card(
              child: Column(
                children: [
                  ListTile(
                    title: Text(investments[index].fund,
                        style: const TextStyle(
                            fontSize: 20, fontWeight: FontWeight.bold)),
                    trailing: Text(
                      '${investments[index].totalValue}\$',
                      style: const TextStyle(
                          fontSize: 20, fontWeight: FontWeight.bold),
                    ),
                  ),
                ],
              ),
            );
          },
        ),
      ),
    );
  }
}
