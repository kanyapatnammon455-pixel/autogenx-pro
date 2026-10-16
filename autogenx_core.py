import json

class AutoGenXCoreEngine:
    def __init__(self, ai_provider="free_local", api_key=None):
        """
        ระบบประมวลผลหลักของ AutoGenX PRO
        :param ai_provider: เลือก AI Engine ('gemini', 'chatgpt', 'grok', 'free_local')
        :param api_key: รหัส API Key (หากไม่มีจะรันด้วยระบบ Local Simulator อัตโนมัติ)
        """
        self.ai_provider = ai_provider.lower()
        self.api_key = api_key
        print(f"[*] เริ่มต้นระบบ AutoGenX PRO - Engine: {self.ai_provider.upper()}")

    def generate_full_package(self, product_name: str, target_platforms: list) -> dict:
        """
        ฟังก์ชันสร้างแพ็กเกจสคริปต์วิดีโอ 4 ขั้นตอน และแคปชันสำหรับโพสต์
        
        :param product_name: ชื่อสินค้าหรือรายละเอียด
        :param target_platforms: แพลตฟอร์มที่ต้องการ ['TikTok', 'Shopee', 'Facebook', 'Instagram', 'YouTube']
        :return: ข้อมูลแพ็กเกจคอนเทนต์พร้อมใช้งาน
        """
        # 1. จัดทำสคริปต์วิดีโอ 4 ขั้นตอน (Storyboard)
        storyboard = {
            "step_1_product_hero": f"🎬 [Product Hero] เปิดตัวหยุดหมุนฟีด (0-3s): 'หยุดดูตรงนี้! {product_name} ตัวเด็ดที่ทุกคนตามหา'",
            "step_2_detail": f"🔍 [Detail] รายละเอียดสินค้า (3-7s): 'เจาะลึกความคุ้มค่าและจุดเด่นของ {product_name}'",
            "step_3_usage": f"💡 [Usage] สาธิตการใช้งาน (7-12s): 'โชว์การใช้จริงให้เห็นผลลัพธ์ชัดเจนเข้าใจง่าย'",
            "step_4_final_shot": f"🛒 [Final Shot] กระตุ้นยอดขาย (12-15s): 'พิกัดตะกร้าเหลือง/ลิงก์หน้าโปรไฟล์ กดสั่งด่วนก่อนของหมด!'"
        }

        # 2. จัดรูปแบบแคปชันแยกตามแพลตฟอร์ม
        captions = {}
        for platform in target_platforms:
            p = platform.lower()
            if "tiktok" in p:
                captions["TikTok"] = (
                    f"🔥 ป้ายยาแรงมากแม่! {product_name} ของมันต้องมีติดบ้าน\n"
                    f"พิกัดกดที่ตะกร้าเหลืองซ้ายมือเลยจ้า 🛒\n\n"
                    f"#TikTokShop #คุณนายสายอีสาน #รีวิวของดีบอกต่อ #{product_name.replace(' ', '')}"
                )
            elif "shopee" in p:
                captions["Shopee"] = (
                    f"🛒 ช้อปด่วน! {product_name} การันตีคุณภาพ ราคาดีที่สุด\n"
                    f"กดใส่ตะกร้าแล้วเก็บโค้ดส่วนลดเพิ่มได้เลยคลิก! 🏷️\n\n"
                    f"#ShopeeTH #ShopeeSocial #ป้ายยาShopee"
                )
            elif "facebook" in p:
                captions["Facebook"] = (
                    f"✨ แนะนำ {product_name} ใช้เองแล้วชอบมาก อยากบอกต่อค่ะ\n"
                    f"สนใจสั่งซื้อหรือสอบถาม ทักแชตเพจได้เลยนะคะ 💌\n\n"
                    f"#FacebookReels #รีวิวสินค้า #คุณนายสายอีสาน"
                )
            elif "instagram" in p:
                captions["Instagram"] = (
                    f"✨ {product_name} Item เด็ดประจำวัน!\n"
                    f"สั่งซื้อคลิกลิงก์หน้า Bio ได้เลยค่ะ 🛍️\n\n"
                    f"#IGShop #ReelsInstagram #คุณนายสายอีสาน"
                )
            elif "youtube" in p:
                captions["YouTube"] = (
                    f"🎬 รีวิว {product_name} แบบสั้นจัดเต็ม!\n"
                    f"พิกัดสั่งซื้อใส่ไว้ในคอมเมนต์ปักหมุดแล้วครับ 📌\n\n"
                    f"#YouTubeShorts #Shorts #รีวิว"
                )

        # 3. รวบรวมข้อมูลส่งกลับ
        return {
            "status": "success",
            "selected_ai": self.ai_provider,
            "product_name": product_name,
            "storyboard_4_steps": storyboard,
            "ready_captions": captions
        }

# --- ส่วนทดสอบการทำงานของโค้ด (Test Execution) ---
if __name__ == "__main__":
    # ทดสอบเรียกใช้ในระบบ Local (สายฟรี 100%)
    app = AutoGenXCoreEngine(ai_provider="free_local")
    
    result = app.generate_full_package(
        product_name="ทิชชู่ห่อหนาพิเศษ (ดึงจากข้างล่างห่อ)",
        target_platforms=["TikTok", "Shopee", "Facebook", "Instagram", "YouTube"]
    )
    
    print("\n=== ผลลัพธ์แพ็กเกจคอนเทนต์ AutoGenX PRO ===")
    print(json.dumps(result, indent=4, ensure_ascii=False))
