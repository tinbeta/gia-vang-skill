#!/usr/bin/env python3
"""
Lấy giá vàng từ PNJ API
Usage: python3 gia_vang.py [options]
"""

import subprocess
import json
import argparse
import sys

def fetch_gold_price():
    """Fetch gold price from PNJ API using curl"""
    url = "https://edge-api.pnj.io/ecom-frontend/v3/get-gold-price"
    
    try:
        result = subprocess.run(
            ['curl', '-s', '-H', 'Accept: application/json', '-H', 'Origin: https://www.giavang.pnj.com.vn', url],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode != 0:
            print(f"❌ Lỗi khi gọi API: {result.stderr}", file=sys.stderr)
            sys.exit(1)
        
        return json.loads(result.stdout)
    except subprocess.TimeoutExpired:
        print("❌ Timeout khi lấy dữ liệu", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Lỗi parse JSON: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Lỗi: {e}", file=sys.stderr)
        sys.exit(1)

def display_all(data):
    """Display all gold prices"""
    print(f"\n🥇 {data['updated_text']}")
    print("─" * 50)
    
    for location in data['locations']:
        name = location['name']
        print(f"\n📍 {name}")
        
        for gold in location['gold_type']:
            gia_mua = gold['gia_mua']
            gia_ban = gold['gia_ban']
            print(f"  {gold['name']}: Mua {gia_mua} | Bán {gia_ban}")

def display_location(data, location_name):
    """Display gold prices for specific location"""
    print(f"\n🥇 {data['updated_text']}")
    print("─" * 50)
    
    found = False
    for location in data['locations']:
        if location_name.lower() in location['name'].lower():
            print(f"\n📍 {location['name']}")
            for gold in location['gold_type']:
                print(f"  {gold['name']}: Mua {gold['gia_mua']} | Bán {gold['gia_ban']}")
            found = True
    
    if not found:
        print(f"❌ Không tìm thấy khu vực: {location_name}")

def display_by_type(data, gold_type):
    """Display gold prices by type (PNJ/SJC)"""
    print(f"\n🥇 {data['updated_text']} - {gold_type.upper()}")
    print("─" * 50)
    
    for location in data['locations']:
        print(f"\n📍 {location['name']}")
        for gold in location['gold_type']:
            if gold_type.upper() in gold['name'].upper():
                print(f"  Mua: {gold['gia_mua']} | Bán: {gold['gia_ban']}")

def display_jewelry(data):
    """Display jewelry gold prices only"""
    print(f"\n🥇 {data['updated_text']} - Vàng nữ trang")
    print("─" * 50)
    
    for location in data['locations']:
        if "nữ trang" in location['name']:
            print(f"\n📍 {location['name']}")
            for gold in location['gold_type']:
                print(f"  {gold['name']}: Mua {gold['gia_mua']} | Bán {gold['gia_ban']}")
            return

def main():
    parser = argparse.ArgumentParser(description='Lấy giá vàng từ PNJ')
    parser.add_argument('--location', '-l', help='Khu vực (TPHCM, Hà Nội, Đà Nẵng...)')
    parser.add_argument('--type', '-t', choices=['PNJ', 'SJC'], help='Loại vàng (PNJ hoặc SJC)')
    parser.add_argument('--jewelry', '-j', action='store_true', help='Chỉ hiển thị vàng nữ trang')
    parser.add_argument('--json', action='store_true', help='Output dạng JSON')
    
    args = parser.parse_args()
    
    data = fetch_gold_price()
    
    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return
    
    if args.jewelry:
        display_jewelry(data)
    elif args.location:
        display_location(data, args.location)
    elif args.type:
        display_by_type(data, args.type)
    else:
        display_all(data)

if __name__ == "__main__":
    main()
