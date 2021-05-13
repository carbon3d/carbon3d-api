import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { PrinterTableComponent } from './printer-table/printer-table.component';
import {ApiConfiguration} from 'src/api/api-configuration';

@NgModule({
  declarations: [
    AppComponent,
    PrinterTableComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
  // Change api root url to use local proxy
  // this prevents CORS issues
  // - see proxyconfig.js
  constructor(apiConfiguration: ApiConfiguration) {
    apiConfiguration.rootUrl = '/api/v1';
  }
 }
