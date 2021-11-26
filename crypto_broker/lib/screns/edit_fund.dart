import 'package:crypto_client/models/asset.dart';
import 'package:crypto_client/models/coin.dart';
import 'package:crypto_client/providers/funds.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:provider/provider.dart';

// a widget that takes fundId as a parameter, then it calls updateAssets(fundId) and then it shows the list of assets with editable field fundPercent

class EditFundScreen extends StatefulWidget {
  final int fundId;
  List<AssetModel> assets;
  EditFundScreen({required this.fundId, required this.assets});
  @override
  _EditFundScreenState createState() => _EditFundScreenState();
}

class _EditFundScreenState extends State<EditFundScreen> {
  // create a form key
  final _formKey = GlobalKey<FormState>();
  late int item;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.add),
        onPressed: () async {
          await Provider.of<FundsProvider>(context, listen: false)
              .getAllCoins();
          final coins = Provider.of<FundsProvider>(context, listen: false)
              .coins
              .map((e) => DropdownMenuItem(
                    child: Text(e.name),
                    value: e.id,
                  ))
              .toList();
          print(coins);
          item = coins.first.value ?? 1;

          // open dialog with drodown button with values from Provider.of<FundsProvider>(context, listen: false).coins
          showDialog(
              context: context,
              builder: (context) {
                return AlertDialog(
                  title: Text('Add Asset'),
                  content: Column(
                    children: [
                      DropdownButton(
                        value: item,
                        items: coins,
                        onChanged: (value) {
                          setState(() {
                            item = value as int;
                            print(item);
                          });
                        },
                      ),
                      TextButton(
                          onPressed: () async {
                            // get the fundPercent sum of widget.assets
                            double sum = 0;
                            widget.assets.forEach((e) {
                              sum += e.fundPercent;
                            });
                            widget.assets.add(AssetModel(
                                id: item,
                                totalValue: 0,
                                coinAmount: 0,
                                fundPercent: 100 - sum,
                                coin: '',
                                fund: widget.fundId));
                            await Provider.of<FundsProvider>(context,
                                    listen: false)
                                .updateAssets(widget.fundId, widget.assets);
                            Navigator.of(context).pop();
                          },
                          child: Text('Add'))
                    ],
                  ),
                );
              });
        },
      ),
      appBar: AppBar(
        title: const Text("Edit Assets of Fund"),
        actions: <Widget>[
          IconButton(
            icon: const Icon(Icons.check),
            onPressed: () {
              if (_formKey.currentState!.validate()) {
                _formKey.currentState!.save();
                // call updateAssets
                Provider.of<FundsProvider>(context, listen: false)
                    .updateAssets(widget.fundId, widget.assets);
                Navigator.of(context).pop();
              } else {
                print("form is not valid");
              }
            },
          ),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(8.0),
        child: RefreshIndicator(
          onRefresh: () async {
            await Provider.of<FundsProvider>(context, listen: false)
                .getAssetsOfFund(widget.fundId);
            setState(() {
              widget.assets =
                  Provider.of<FundsProvider>(context, listen: false).assets;
            });
          },
          child: Form(
            key: _formKey,
            child: ListView.builder(
              itemCount: Provider.of<FundsProvider>(context, listen: false)
                  .assets
                  .length,
              itemBuilder: (context, index) {
                return Column(
                  children: <Widget>[
                    ListTile(
                      title: Text(
                        'Name: ${widget.assets[index].coin}',
                        style: const TextStyle(
                          fontSize: 20,
                        ),
                      ),
                      subtitle: Text(
                        'amount: ${widget.assets[index].coinAmount.toString()}',
                        style: const TextStyle(
                          fontSize: 15,
                        ),
                      ),
                      trailing: Text(
                        '${widget.assets[index].totalValue.toString()} PLN',
                        style: const TextStyle(
                          fontSize: 15,
                        ),
                      ),
                    ),
                    const Divider(
                      height: 2,
                    ),
                    TextFormField(
                        decoration: const InputDecoration(
                          labelText: 'Percentage',
                        ),
                        initialValue:
                            widget.assets[index].fundPercent.toString(),
                        keyboardType: TextInputType.number,
                        onChanged: (value) {
                          widget.assets[index].fundPercent =
                              double.parse(value);
                        },
                        autovalidateMode: AutovalidateMode.always,
                        validator: (value) {
                          if (value == null || value.isEmpty) {
                            return 'Please enter some text';
                          }
                          if (value.isNotEmpty && double.parse(value) > 100) {
                            return 'Percentage cannot be more than 100';
                          }
                          // sum of all the percentages should be 100
                          double sum = 0;
                          for (int i = 0; i < widget.assets.length; i++) {
                            sum += widget.assets[i].fundPercent;
                          }
                          if (sum != 100) {
                            return 'Sum of percentages should be 100';
                          }
                          return null;
                        }),
                  ],
                );
              },
            ),
          ),
        ),
      ),
    );
  }
}
