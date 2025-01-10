import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TwentiethItemComponent } from './twentieth-item.component';

describe('TwentiethItemComponent', () => {
  let component: TwentiethItemComponent;
  let fixture: ComponentFixture<TwentiethItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [TwentiethItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TwentiethItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
