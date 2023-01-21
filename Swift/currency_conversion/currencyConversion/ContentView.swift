//
//  ContentView.swift
//  currencyConversion
//
//  Created by Saurav Dwivedi on 2023-01-19.
//

import SwiftUI

struct ContentView: View {
    @EnvironmentObject var network: Network
    
    var body: some View {
        VStack(alignment: .center) {
            Text("SEK to INR conversion")
                .font(.title)
                .bold()
            
            VStack(alignment: .leading) {
                HStack(alignment:.top) {
                    Text("1 SEK =")
                    Text("\(network.response.result)").bold()
                    Text("INR")
                }
                .frame(width: 300, alignment: .center)
                .padding()
                .background(Color(#colorLiteral(red: 0.6667672396, green: 0.7527905703, blue: 1, alpha: 0.2662717301)))
                .cornerRadius(20)
                .onAppear {
                    network.getExchangeRate()
                }
            }
            .padding(.vertical)
            .onAppear {
                network.getExchangeRate()
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
            .environmentObject(Network())
    }
}
