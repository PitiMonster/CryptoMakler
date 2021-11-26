import 'package:crypto_client/providers/funds.dart';
import 'package:crypto_client/screns/edit_fund.dart';
import 'package:crypto_client/screns/invitation_screen.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'dart:math' as math;
import 'package:provider/provider.dart';

class FundsScreen extends StatefulWidget {
  FundsScreen({Key? key}) : super(key: key);

  @override
  _FundsScreenState createState() => _FundsScreenState();
}

class _FundsScreenState extends State<FundsScreen> {
  @override
  void initState() {
    Provider.of<FundsProvider>(context, listen: false).fetchFunds();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    final funds = Provider.of<FundsProvider>(context).funds;

    return Scaffold(
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.add),
        onPressed: () async {
          Navigator.pushNamed(context, '/add-funds');
        },
      ),
      //create appbar with two TextButtons
      appBar: AppBar(
        title: const Text('Funds'),
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
          await Provider.of<FundsProvider>(context, listen: false).fetchFunds();
        },
        child: ListView.builder(
          itemCount: funds.length,
          itemBuilder: (context, index) {
            return Card(
              child: Column(
                children: [
                  ListTile(
                    title: Text(funds[index].name,
                        style: const TextStyle(
                            fontSize: 20, fontWeight: FontWeight.bold)),
                    leading: Text('${funds[index].fee}%',
                        style: const TextStyle(fontSize: 16)),
                    subtitle: Text('${funds[index].totalValue}\$'),
                    trailing: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        IconButton(
                          onPressed: () async {
                            await Provider.of<FundsProvider>(context,
                                    listen: false)
                                .getAssetsOfFund(funds[index].id);
                            Navigator.push(
                              context,
                              MaterialPageRoute(
                                builder: (context) => EditFundScreen(
                                  fundId: funds[index].id,
                                  assets: Provider.of<FundsProvider>(context, listen: false)
                                      .assets,
                                ),
                              ),
                            );
                          },
                          icon: const Icon(Icons.edit),
                        ),
                        IconButton(
                          icon: const Icon(Icons.person_add),
                          onPressed: () {
                            Navigator.of(context).push(
                              MaterialPageRoute(
                                builder: (context) => InvitationScreen(
                                  fund: funds[index].id,
                                ),
                              ),
                            );
                          },
                        ),
                      ],
                    ),
                  ),
                  Container(
                    height: 1,
                    color: Colors.white,
                  ),
                  ExpansionTile(
                    title: const Text('Investors'),
                    children: <Widget>[
                      SizedBox(
                        height:
                            math.min(150, funds[index].investors.length * 50),
                        child: ListView.builder(
                          itemCount: funds[index].investors.length,
                          itemBuilder: (context, i) {
                            return ListTile(
                              title: Text(funds[index].investors[i].investor),
                              trailing: Text(
                                  '${funds[index].investors[i].shareAmount}\$'),
                            );
                          },
                        ),
                      ),
                    ],
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
