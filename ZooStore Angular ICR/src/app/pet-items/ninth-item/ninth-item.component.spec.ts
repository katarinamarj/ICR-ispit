import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NinthItemComponent } from './ninth-item.component';

describe('NinthItemComponent', () => {
  let component: NinthItemComponent;
  let fixture: ComponentFixture<NinthItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [NinthItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NinthItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
