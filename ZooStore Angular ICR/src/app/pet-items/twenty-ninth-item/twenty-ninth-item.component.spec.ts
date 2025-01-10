import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TwentyNinthItemComponent } from './twenty-ninth-item.component';

describe('TwentyNinthItemComponent', () => {
  let component: TwentyNinthItemComponent;
  let fixture: ComponentFixture<TwentyNinthItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [TwentyNinthItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TwentyNinthItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
