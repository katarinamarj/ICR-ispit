import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { SignupComponent } from './auth/signup/signup.component';
import { LoginComponent } from './auth/login/login.component';
import { CartComponent } from './cart/cart.component';
import { UserpanelComponent } from './auth/userpanel/userpanel.component';
import { CatalogComponent } from './catalog/catalog.component';
import { ReviewComponent } from './review/review.component';
import { AuthGuard } from './auth.guard';
import { PaymentComponent } from './payment/payment.component';
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



const routes: Routes = [
  { path: '', component: HomeComponent }, 
  { path: 'signup', component: SignupComponent },
  { path: 'login', component: LoginComponent },
  { path: 'cart', component: CartComponent },
  { path: 'userpanel', component: UserpanelComponent, canActivate: [AuthGuard] },
  { path: 'catalog', component: CatalogComponent },
  { path: 'review', component: ReviewComponent },
  { path: 'payment', component: PaymentComponent },
  { path: 'first', component: FirstItemComponent },
  { path: 'second', component: SecondItemComponent },
  { path: 'third', component: ThirdItemComponent },
  { path: 'fourth', component: FourthItemComponent },
  { path: 'fifth', component: FifthItemComponent },
  { path: 'sixth', component: SixthItemComponent },
  { path: 'seventh', component: SeventhItemComponent },
  { path: 'eighth', component: EighthItemComponent },
  { path: 'ninth', component: NinthItemComponent },
  { path: 'tenth', component: TenthItemComponent },
  { path: 'eleventh', component: EleventhItemComponent },
  { path: 'twelfth', component: TwelfthItemComponent },
  { path: 'thirteenth', component: ThirteenthItemComponent },
  { path: 'fourteenth', component: FourteenthItemComponent },
  { path: 'fifteenth', component: FifteenthItemComponent },
  { path: 'sixteenth', component: SixteenthItemComponent },
  { path: 'seventeenth', component: SeventeenthItemComponent },
  { path: 'eighteenth', component: EighteenthItemComponent },
  { path: 'nineteenth', component: NineteenthItemComponent },
  { path: 'twentieth', component: TwentiethItemComponent },
  { path: 'twenty-first', component: TwentyFirstItemComponent },
  { path: 'twenty-second', component: TwentySecondItemComponent },
  { path: 'twenty-third', component: TwentyThirdItemComponent },
  { path: 'twenty-fourth', component: TwentyFourthItemComponent },
  { path: 'twenty-fifth', component: TwentyFifthItemComponent },
  { path: 'twenty-sixth', component: TwentySixthItemComponent },
  { path: 'twenty-seventh', component: TwentySeventhItemComponent },
  { path: 'twenty-eighth', component: TwentyEighthItemComponent },
  { path: 'twenty-ninth', component: TwentyNinthItemComponent },
  { path: 'thirtieth', component: ThirtiethItemComponent },
  { path: '**', redirectTo: '', pathMatch: 'full' }  // Ovo je catch-all ruta za sve nepostojeće rute
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
