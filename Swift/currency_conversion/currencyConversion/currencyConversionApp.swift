//
//  currencyConversionApp.swift
//  currencyConversion
//
//  Created by Saurav Dwivedi on 2023-01-19.
//

import SwiftUI

@main
struct currencyConversionApp: App {
    var network = Network()
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(network)
        }
    }
}

import SwiftUI

