const foods = ["Піца", "Борщ", "Салат", "Паста", "Риба"];

function randomFood() {
  const index = Math.floor(Math.random() * foods.length);
  return foods[index];
}

function generateMenu() {
  console.log("Меню на сьогодні:");
  console.log("Страва:", randomFood());
}

generateMenu();