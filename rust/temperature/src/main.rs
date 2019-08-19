use std::io;
 
fn main() {
    select_conversion()
}
 
fn select_conversion() {
 
    let mut answer = String::new();

    println!("Would you like to convert from Celsius to Fahrenheit (press C) or from Fahrenheit to Celsius! (press F)");
   
    io::stdin().read_line(&mut answer)
        .expect("Failed to read line");
   
    if answer.trim().eq("C")  {
        println!("Give degrees in Celsius");
        let degree = read_number();
        let converted = convert_celsius_to_fahrenheit(degree);
        println!("{} degrees in Celsius is {} degrees in Fahrenheit.",degree,converted)
    } else if answer.trim().eq("F") {
        println!("Give degrees in Fahrenheit");
        let degree = read_number();
        let converted = convert_fahrenheit_to_celsius(degree);
           println!("{} degrees in Fahrenheit is {} degrees in Celsius.",degree,converted)
    } else {
        println!("answer was {}", answer);
        println!("Give C or F");
    }
}
 
fn read_number() -> f64 {
    let mut number = String::new();
 
    io::stdin().read_line(&mut number)
        .expect("Failed to read line");
 
    let  number: f64 = number.trim().parse()
        .expect("Please type a number!");
    number
}
 
fn convert_celsius_to_fahrenheit(x: f64) -> f64 {
    (x * 1.8) + 32.0
}
 
fn convert_fahrenheit_to_celsius(x: f64) -> f64 {
    (x - 32.0)/(1.8)
}