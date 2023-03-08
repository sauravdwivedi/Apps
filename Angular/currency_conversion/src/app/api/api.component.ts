import { Component, OnInit } from '@angular/core';
import { ApiService } from './api.service';
import { FormGroup, FormControl } from '@angular/forms';
import { CurrenciesSchema } from './api.service';
import {
    ApexAxisChartSeries,
    ApexChart,
    ApexTitleSubtitle,
    ApexDataLabels,
    ApexFill,
    ApexMarkers,
    ApexYAxis,
    ApexXAxis,
    ApexTooltip
} from "ng-apexcharts";


@Component({
    selector: 'app-api',
    templateUrl: './api.component.html',
    styleUrls: ['./api.component.css']
})

export class ApiComponent implements OnInit {
    title = 'Currency conversion historical data';
    selectedCurrencyOne: string = "SEK";
    selectedCurrencyTwo: string = "INR";
    maxDate: Date;
    currenciesList = new CurrenciesSchema();
    currencies: string[] = ["SEK", "INR", "EUR"];
    range = new FormGroup({
        start: new FormControl<Date | null>(null),
        end: new FormControl<Date | null>(null),
    });
    dataPoints: [number, number][] = [];

    constructor(private apiService: ApiService) {
    }

    ngOnInit() {
        this.getCurrencies();
        this.maxDate = new Date();
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
        startDate.setHours(startDate.getHours() + 1);
        let endDate: Date = this.range.value.end!;
        endDate.setHours(endDate.getHours() + 1);

        this.apiService.getExchangeData(
            this.selectedCurrencyOne,
            this.selectedCurrencyTwo,
            startDate,
            endDate
        )
            .subscribe(data => {
                console.log(data);
                this.dataPoints = [];
                let rates = data.rates;
                let dates = Object.keys(rates)
                let values: { String: Number }[] = Object.values(rates)
                for (let i = 0; i < values.length; i++) {
                    this.dataPoints.push([new Date(dates[i]).getTime(), Number(Object.values(values[i])[0])]);
                    this.initChartData();
                }
            });
    }

    refresh() {
        this.initChartData();
        // window.location.reload();
    }

    public series: ApexAxisChartSeries;
    public chart: ApexChart;
    public dataLabels: ApexDataLabels;
    public markers: ApexMarkers;
    public titleChart: ApexTitleSubtitle;
    public fill: ApexFill;
    public yaxis: ApexYAxis;
    public xaxis: ApexXAxis;
    public tooltip: ApexTooltip;

    public initChartData(): void {
        this.series = [
            {
                name: `${this.selectedCurrencyTwo}`,
                data: this.dataPoints
            }
        ];
        this.chart = {
            type: "area",
            stacked: false,
            height: 350,
            zoom: {
                type: "x",
                enabled: true,
                autoScaleYaxis: true
            },
            toolbar: {
                autoSelected: "zoom"
            }
        };
        this.dataLabels = {
            enabled: false
        };
        this.markers = {
            size: 0
        };
        this.titleChart = {
            text: `${this.selectedCurrencyOne} to ${this.selectedCurrencyTwo} exchange rate historical data`,
            align: "center"
        };
        this.fill = {
            type: "gradient",
            gradient: {
                shadeIntensity: 1,
                inverseColors: false,
                opacityFrom: 0.5,
                opacityTo: 0,
                stops: [0, 90, 100]
            }
        };
        this.yaxis = {
            labels: {
                formatter: function (val) {
                    return (val).toFixed(2);
                }
            },
            title: {
                text: `${this.selectedCurrencyOne} to ${this.selectedCurrencyTwo} exchange rate`
            }
        };
        this.xaxis = {
            type: "datetime"
        };
        this.tooltip = {
            shared: false,
            y: {
                formatter: function (val) {
                    return (val).toFixed(2);
                }
            }
        };
    }
}