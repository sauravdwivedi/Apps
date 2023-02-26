import { Component, OnInit } from '@angular/core';
import { ApiService } from './api.service';
import { FormGroup, FormControl } from '@angular/forms';
import { CurrenciesSchema } from './api.service';


@Component({
    selector: 'app-api',
    templateUrl: './api.component.html',
    styleUrls: ['./api.component.css']
})

export class ApiComponent implements OnInit {
    title = 'Currency conversion historical data';
    selectedCurrencyOne: string = "SEK";
    selectedCurrencyTwo: string = "INR";
    currenciesList = new CurrenciesSchema();
    currencies: string[] = ["SEK", "INR", "EUR"];
    range = new FormGroup({
        start: new FormControl<Date | null>(null),
        end: new FormControl<Date | null>(null),
    });
    dataPoints: DataPoint[] = [];
    chart: any;

    constructor(private apiService: ApiService) { }

    ngOnInit() {
        this.getCurrencies();
    }

    getChartInstance(chart: object) {
        this.chart = chart;
    }

    getCurrencies() {
        this.apiService.getCurrencies()
            .subscribe(data => {
                console.log(data)
                this.currenciesList.success = data.success;
                this.currenciesList.currencies = Object.keys(data.currencies);
                this.currencies = this.currenciesList.currencies;
            })

    }

    getExchangeData() {
        let startDate: Date = this.range.value.start!;
        startDate.setDate(startDate.getDate() + 1);
        let endDate: Date = this.range.value.end!;
        endDate.setDate(endDate.getDate() + 1);

        this.apiService.getExchangeData(
            this.selectedCurrencyOne,
            this.selectedCurrencyTwo,
            startDate,
            endDate
        )
            .subscribe(data => {
                console.log(data);
                let rates = data.rates;
                let dates = Object.keys(rates)
                let values: { String: Number }[] = Object.values(rates)
                for (let i = 0; i < values.length; i++) {
                    this.dataPoints.push({ x: new Date(dates[i]), y: Number(Object.values(values[i])[0]) });
                }
                this.chart.subtitles[0].remove();
            })
        this.chart.render();
    }

    chartOptions = {
        theme: "light2",
        zoomEnabled: true,
        animationEnabled: true,
        exportEnabled: true,
        title: {
            text: "Exchange rate historical data"
        },
        subtitles: [{
            text: "Loading Data...",
            fontSize: 24,
            horizontalAlign: "center",
            verticalAlign: "center",
            dockInsidePlotArea: true
        }],
        axisY: {
            title: "Exchange Rate",
        },
        data: [{
            type: "spline",
            name: "Exchange Rate",
            yValueFormatString: "#,###.00",
            xValueType: "dateTime",
            dataPoints: this.dataPoints
        }]
    }

    refresh() {
        window.location.reload();
    }
}
type DataPoint = {
    x: Date;
    y: Number;
}
