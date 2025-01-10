import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SignupComponent } from './auth/signup/signup.component';
import { LoginComponent } from './auth/login/login.component';
import { HomeComponent } from './home/home.component';
import { CartComponent } from './cart/cart.component';
import { UserpanelComponent } from './auth/userpanel/userpanel.component';
import { CatalogComponent } from './catalog/catalog.component';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { MaterialModule } from './ui-material.module';
import { FlexLayoutModule } from '@ngbracket/ngx-layout';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ReviewComponent } from './review/review.component';
import { AuthService } from './auth.service';
import { AuthGuard } from './auth.guard';
import { PaymentComponent } from './payment/payment.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { MarkdownModule } from 'ngx-markdown';
import { MatToolbarModule } from '@angular/material/toolbar';
import { FirstItemComponent } from './pet-items/first-item/first-item.component';
import { SecondItemComponent } from './pet-items/second-item/second-item.component';
import { ThirdItemComponent } from './pet-items/third-item/third-item.component';
import { FourthItemComponent } from './pet-items/fourth-item/fourth-item.component';
import { FifthItemComponent } from './pet-items/fifth-item/fifth-item.component';
import { SixthItemComponent } from './pet-items/sixth-item/sixth-item.component';
import { SeventhItemComponent } from './pet-items/seventh-item/seventh-item.component';
import { EighthItemComponent } from './pet-items/eighth-item/eighth-item.component';
import { NinthItemComponent } from './pet-items/ninth-item/ninth-item.component';
import { TenthItemComponent } from './pet-items/tenth-item/tenth-item.component';
import { EleventhItemComponent } from './pet-items/eleventh-item/eleventh-item.component';
import { TwelfthItemComponent } from './pet-items/twelfth-item/twelfth-item.component';
import { ThirteenthItemComponent } from './pet-items/thirteenth-item/thirteenth-item.component';
import { FourteenthItemComponent } from './pet-items/fourteenth-item/fourteenth-item.component';
import { FifteenthItemComponent } from './pet-items/fifteenth-item/fifteenth-item.component';
import { SixteenthItemComponent } from './pet-items/sixteenth-item/sixteenth-item.component';
import { SeventeenthItemComponent } from './pet-items/seventeenth-item/seventeenth-item.component';
import { EighteenthItemComponent } from './pet-items/eighteenth-item/eighteenth-item.component';
import { NineteenthItemComponent } from './pet-items/nineteenth-item/nineteenth-item.component';
import { TwentiethItemComponent } from './pet-items/twentieth-item/twentieth-item.component';
import { TwentyFirstItemComponent } from './pet-items/twenty-first-item/twenty-first-item.component';
import { TwentySecondItemComponent } from './pet-items/twenty-second-item/twenty-second-item.component';
import { TwentyThirdItemComponent } from './pet-items/twenty-third-item/twenty-third-item.component';
import { TwentyFourthItemComponent } from './pet-items/twenty-fourth-item/twenty-fourth-item.component';
import { TwentyFifthItemComponent } from './pet-items/twenty-fifth-item/twenty-fifth-item.component';
import { TwentySixthItemComponent } from './pet-items/twenty-sixth-item/twenty-sixth-item.component';
import { TwentySeventhItemComponent } from './pet-items/twenty-seventh-item/twenty-seventh-item.component';
import { TwentyEighthItemComponent } from './pet-items/twenty-eighth-item/twenty-eighth-item.component';
import { TwentyNinthItemComponent } from './pet-items/twenty-ninth-item/twenty-ninth-item.component';
import { ThirtiethItemComponent } from './pet-items/thirtieth-item/thirtieth-item.component';




@NgModule({
  declarations: [
    AppComponent, 
    SignupComponent,
    LoginComponent,
    HomeComponent, 
    CartComponent,
    UserpanelComponent,
    CatalogComponent,
    ReviewComponent,
    PaymentComponent,
    FirstItemComponent,
    SecondItemComponent,
    ThirdItemComponent,
    FourthItemComponent,
    FifthItemComponent,
    SixthItemComponent,
    SeventhItemComponent,
    EighthItemComponent,
    NinthItemComponent,
    TenthItemComponent,
    EleventhItemComponent,
    TwelfthItemComponent,
    ThirteenthItemComponent,
    FourteenthItemComponent,
    FifteenthItemComponent,
    SixteenthItemComponent,
    SeventeenthItemComponent,
    EighteenthItemComponent,
    NineteenthItemComponent,
    TwentiethItemComponent,
    TwentyFirstItemComponent,
    TwentySecondItemComponent,
    TwentyThirdItemComponent,
    TwentyFourthItemComponent,
    TwentyFifthItemComponent,
    TwentySixthItemComponent,
    TwentySeventhItemComponent,
    TwentyEighthItemComponent,
    TwentyNinthItemComponent,
    ThirtiethItemComponent

  ],
  
  imports: [
    BrowserModule,
    AppRoutingModule,
    MaterialModule,
    FlexLayoutModule,
    FormsModule,
    BrowserAnimationsModule,
    ReactiveFormsModule,
    HttpClientModule,
    MarkdownModule,
    MatToolbarModule
  ],
  providers: [
    provideAnimationsAsync(),
    AuthGuard,
    AuthService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
