import { Component } from '@angular/core';
import { CartService } from '../cart.service';
import {MatSliderModule} from '@angular/material/slider';
import { debounceTime, distinctUntilChanged } from 'rxjs/operators';
import { Subject } from 'rxjs';


@Component({
  selector: 'app-catalog',
  templateUrl: './catalog.component.html',
  styleUrl: './catalog.component.css'
  
})
export class CatalogComponent {
viewDetails(arg0: any) {
throw new Error('Method not implemented.');
}

  products = [
    { id: 1, name: 'Rex', type: 'Dog', color: 'Orange', age: '3', size: 'Small', origin: 'Germany', price: 100, review: '5 stars', image: 'https://thumbs.dreamstime.com/b/beautiful-happy-reddish-havanese-puppy-dog-sitting-frontal-looking-camera-isolated-white-background-46868560.jpg', showDetails: false },
    { id: 2, name: 'Fluffy', type: 'Hamster', color: 'Brown', age: '1', size: 'Small', origin: 'USA', price: 10, review: '4 stars', image: 'https://img.pikbest.com/origin/09/29/39/52WpIkbEsTqAj.png!sw800', showDetails: false },
    { id: 3, name: 'Whiskers', type: 'Cat', color: 'Orange', age: '2', size: 'Medium', origin: 'France', price: 80, review: '5 stars', image: 'https://img.freepik.com/free-photo/red-white-cat-i-white-studio_155003-13189.jpg?w=360', showDetails: false },
    { id: 4, name: 'Bubbles', type: 'Fish', color: 'Gold', age: '1', size: 'Small', origin: 'Australia', price: 20, review: '4 stars', image: 'https://thumbs.dreamstime.com/b/summer-tropical-reef-fish-collection-isolated-white-background-41688673.jpg', showDetails: false },
    { id: 5, name: 'Sunny', type: 'Parrot', color: 'Yellow', age: '4', size: 'Medium', origin: 'Brazil', price: 150, review: '5 stars', image: 'https://img.freepik.com/premium-vector/free-parrot-png-photo-white-background-generated-ai_1043838-2955.jpg', showDetails: false },
    { id: 6, name: 'Thumper', type: 'Rabbit', color: 'Grey', age: '2', size: 'Small', origin: 'Canada', price: 30, review: '4 stars', image: 'https://media.istockphoto.com/id/959866606/photo/rabbit-4-months-old-sitting-against-white-background.jpg?s=612x612&w=0&k=20&c=8yRFVDIgoXj3gCh7ckkF4gCh8JjWN967r244PQ4vFUU=', showDetails: false },
    { id: 7, name: 'Max', type: 'Dog', color: 'Brown', age: '5', size: 'Medium', origin: 'USA', price: 120, review: '5 stars', image: 'https://www.bil-jac.com/media/sy5jgj4k/dog-leo-min.png?&format=webp&width=400&mode=max&quality=80', showDetails: false },
    { id: 8, name: 'Nibbles', type: 'Hamster', color: 'Brown', age: '1', size: 'Small', origin: 'USA', price: 15, review: '4 stars', image: 'https://st4.depositphotos.com/10614052/41661/i/450/depositphotos_416618198-stock-photo-funny-hamster-white-background.jpg', showDetails: false },
    { id: 9, name: 'Socks', type: 'Cat', color: 'White', age: '3', size: 'Small', origin: 'UK', price: 60, review: '5 stars', image: 'https://thumbs.dreamstime.com/b/turkish-angora-cat-white-background-portrait-animal-themes-front-view-145390427.jpg', showDetails: false },
    { id: 10, name: 'Sky', type: 'Parrot', color: 'Blue', age: '3', size: 'Medium', origin: 'Mexico', price: 140, review: '5 stars', image: 'https://thumbs.dreamstime.com/b/colorful-orange-parrot-macaw-isolated-white-background-35613998.jpg', showDetails: false },
    { id: 11, name: 'Splash', type: 'Fish', color: 'Gold', age: '2', size: 'Small', origin: 'China', price: 25, review: '4 stars', image: 'https://s7d2.scene7.com/is/image/PetSmart/5176556', showDetails: false },
    { id: 12, name: 'Cuddles', type: 'Rabbit', color: 'Gray', age: '2', size: 'Small', origin: 'Germany', price: 35, review: '4 stars', image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRI-a4PNsfOOfJcgEiDfL3QJ5t6NzP8COK_ghmWyG431p6OQz4-V2zUmKfgnAectbgIYXc&usqp=CAU', showDetails: false },
    { id: 13, name: 'Mittens', type: 'Cat', color: 'White', age: '4', size: 'Medium', origin: 'USA', price: 70, review: '5 stars', image: 'https://mascotasya.com/images/mascopedia/224-angora_turco_gato.jpg', showDetails: false },
    { id: 14, name: 'Bolt', type: 'Dog', color: 'Brown', age: '2', size: 'Large', origin: 'Canada', price: 110, review: '4 stars', image: 'https://publish.purewow.net/wp-content/uploads/sites/2/2021/01/low-maintenance-dog-breeds-broholmer.jpg?fit=680%2C860', showDetails: false },
    { id: 15, name: 'Slither', type: 'Snake', color: 'Brown', age: '1', size: 'Small', origin: 'Egypt', price: 90, review: '4 stars', image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRoeLjwuXK-08Bt7tJwDmVuHp1qvdJG_9nDtA&s', showDetails: false },
    { id: 16, name: 'Rio', type: 'Parrot', color: 'Red', age: '5', size: 'Large', origin: 'Brazil', price: 160, review: '5 stars', image: 'https://img.freepik.com/premium-photo/beautiful-parrot-white-background_41532-184.jpg', showDetails: false },
    { id: 17, name: 'Fin', type: 'Fish', color: 'Silver', age: '3', size: 'Medium', origin: 'Japan', price: 30, review: '4 stars', image: 'https://allergy-web-staging.s3.ap-southeast-2.amazonaws.com/wp-content/uploads/Fish_600px_NoBKG.png', showDetails: false },
    { id: 18, name: 'Flopsy', type: 'Rabbit', color: 'White', age: '1', size: 'Medium', origin: 'Australia', price: 40, review: '4 stars', image: 'https://media.istockphoto.com/id/959866606/photo/rabbit-4-months-old-sitting-against-white-background.jpg?s=612x612&w=0&k=20&c=8yRFVDIgoXj3gCh7ckkF4gCh8JjWN967r244PQ4vFUU=', showDetails: false },
    { id: 19, name: 'Zippy', type: 'Hamster', color: 'Grey', age: '2', size: 'Small', origin: 'Canada', price: 18, review: '4 stars', image: 'https://thumbs.dreamstime.com/b/hamster-20009706.jpg', showDetails: false },
    { id: 20, name: 'Sam', type: 'Dog', color: 'Brown', age: '6', size: 'Large', origin: 'Australia', price: 140, review: '5 stars', image: 'https://www.petlandindependence.com/wp-content/uploads/2022/06/Rhodesian-Ridgeback.png', showDetails: false },
    { id: 21, name: 'Cloud', type: 'Parrot', color: 'Yellow', age: '2', size: 'Medium', origin: 'South Africa', price: 150, review: '5 stars', image: 'https://st2.depositphotos.com/2808973/5494/i/450/depositphotos_54941687-stock-photo-bule-gold-yellow-macaw-isolated.jpg', showDetails: false },
    { id: 22, name: 'Shadow', type: 'Snake', color: 'Black', age: '4', size: 'Medium', origin: 'Africa', price: 120, review: '4 stars', image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQa0BH38ggAsyHrj2I9gPtCifwMyTAr_wxM0hLEsENY2A1EIju6FmcrJwpNXiTJtfWXyFE&usqp=CAU', showDetails: false },
    { id: 23, name: 'Chester', type: 'Hamster', color: 'Brown', age: '3', size: 'Small', origin: 'UK', price: 12, review: '5 stars', image: 'https://static3.depositphotos.com/1003283/157/i/450/depositphotos_1574217-stock-photo-hamster.jpg', showDetails: false },
    { id: 24, name: 'Thistle', type: 'Rabbit', color: 'Orange', age: '1', size: 'Small', origin: 'New Zealand', price: 35, review: '4 stars', image: 'https://www.collinsdictionary.com/images/full/rabbit_274039655.jpg', showDetails: false },
    { id: 25, name: 'Fire', type: 'Parrot', color: 'Green', age: '2', size: 'Medium', origin: 'Costa Rica', price: 155, review: '5 stars', image: 'https://st.depositphotos.com/1578496/4368/i/450/depositphotos_43686969-stock-photo-beautiful-green-parrot.jpg', showDetails: false },
    { id: 26, name: 'Star', type: 'Fish', color: 'Blue', age: '1', size: 'Small', origin: 'USA', price: 20, review: '5 stars', image: 'https://img.freepik.com/free-psd/swimming-fish-isolated_23-2151359680.jpg', showDetails: false },
    { id: 27, name: 'Flare', type: 'Cat', color: 'Gray', age: '2', size: 'Medium', origin: 'India', price: 80, review: '5 stars', image: 'https://i.pinimg.com/550x/c1/c4/4a/c1c44a54126f793241da90e3d4c147e3.jpg', showDetails: false },
    { id: 28, name: 'Buddy', type: 'Dog', color: 'Brown', age: '3', size: 'Large', origin: 'France', price: 100, review: '5 stars', image: 'https://img.freepik.com/free-psd/cute-brown-white-dog-scene_23-2150179279.jpg?semt=ais_hybrid', showDetails: false },
    { id: 29, name: 'Viper', type: 'Snake', color: 'Brown', age: '3', size: 'Large', origin: 'India', price: 130, review: '4 stars', image: 'https://img.freepik.com/premium-psd/brown-snake-white-background-isolated-white-transparent-png-generative-ai_130745-271.jpg', showDetails: false },
    { id: 30, name: 'Charlie', type: 'Parrot', color: 'Blue', age: '4', size: 'Large', origin: 'Australia', price: 160, review: '5 stars', image: 'https://i.pinimg.com/236x/06/38/c3/0638c356c1f44f73337824c31307090b.jpg', showDetails: false }
];


filteredProducts: any[] = [...this.products];
searchQuery: string = '';
minPrice: number = 0;
maxPrice: number = 1000;
selectedType: string = '';
selectedSize: string = '';
selectedColor: string = '';
selectedMaterial: string = '';
selectedReview: string = '';

types = [...new Set(this.products.map(product => product.type))];
sizes = [...new Set(this.products.map(product => product.size))];
colors = [...new Set(this.products.map(product => product.color))];

private searchSubject: Subject<string> = new Subject(); 
constructor(private cartService: CartService) {
  this.searchSubject.pipe(
    debounceTime(300),          
    distinctUntilChanged()      
  ).subscribe(query => {
    this.searchQuery = query;  
    this.filterProducts();    
  });
}

toggleDetails(product: any, show: boolean): void {
  product.showDetails = show;
}

addToCart(product: any) {
  this.cartService.addToCart(product);
  alert('Product added to cart!');
}

clearSearch() {
  this.searchQuery = '';
  this.searchSubject.next(''); 
  this.filterProducts();      
}

onSearch() {
  this.searchSubject.next(this.searchQuery); 
}

filterProducts() {
  this.filteredProducts = this.products.filter(product => {
    const matchesSearchQuery = product.type.toLowerCase().includes(this.searchQuery.toLowerCase());
    const matchesPriceRange = product.price >= this.minPrice && product.price <= this.maxPrice;
    const matchesType = this.selectedType ? product.type === this.selectedType : true;
    const matchesSize = this.selectedSize ? product.size === this.selectedSize : true;
    const matchesColor = this.selectedColor ? product.color === this.selectedColor : true;
    return matchesSearchQuery && matchesPriceRange && matchesType && matchesSize && matchesColor;
  });
}

clearFilters() {
  this.searchQuery = '';
  this.minPrice = 0;
  this.maxPrice = 1000;
  this.selectedType = '';
  this.selectedSize = '';
  this.selectedColor = '';
  this.selectedMaterial = '';
  this.selectedReview = '';
  this.filterProducts();
}
  
}
