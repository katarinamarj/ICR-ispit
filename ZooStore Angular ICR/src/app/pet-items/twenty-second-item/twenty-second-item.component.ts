import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-twenty-second-item',
  templateUrl: './twenty-second-item.component.html',
  styleUrl: './twenty-second-item.component.css'
})
export class TwentySecondItemComponent {
  
  product = {
    id: 22,
    name: 'Shadow',
    price: 120,
    type: 'Snake',
    color: 'Black',
    age: '4',
    size: 'Medium',
    origin: 'Africa',
    review: '4 stars',
    image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQa0BH38ggAsyHrj2I9gPtCifwMyTAr_wxM0hLEsENY2A1EIju6FmcrJwpNXiTJtfWXyFE&usqp=CAU'
  };

  constructor(private cartService: CartService, private router: Router) {}

  addToCart(product: any) {
    this.cartService.addToCart(product);
    this.router.navigate(['/cart']);
  }
}
