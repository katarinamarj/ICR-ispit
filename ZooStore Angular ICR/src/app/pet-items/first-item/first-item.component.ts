import { Component } from '@angular/core';
import { CartService } from '../../cart.service';  
import { Router } from '@angular/router';  

@Component({
  selector: 'app-first-item',
  templateUrl: './first-item.component.html',
  styleUrls: ['./first-item.component.css']
})
export class FirstItemComponent {
item: any;
  constructor(
    private cartService: CartService,  
    private router: Router  
  ) {}

  product = {
    id: 1,
    name: 'Rex',
    price: 100,
    type: 'Dog',
    color: 'Orange',
    size: 'Small',
    origin: 'Germany',
    review: '5 stars',
    image: 'https://thumbs.dreamstime.com/b/beautiful-happy-reddish-havanese-puppy-dog-sitting-frontal-looking-camera-isolated-white-background-46868560.jpg'
  };

  addToCart(product: any) {
    this.cartService.addToCart(product); 
    alert('Product added to cart!');
    this.router.navigate(['/cart']);  
  }
  
}
