import os
import json

class AutoGenXEngine:
    def __init__(self, ai_provider="chatgpt"):
        """
        ระบบหลักของ AutoGenX PRO
        :param ai_provider: เลือก AI ที่ต้องการใช้งาน ('chatgpt', 'gemini', 'grok')
        """
        self.ai_provider = ai_provider.lower()
        print(f"[*] เริ่มต้นระบบ AutoGenX PRO ด้วย AI Engine: {self.ai_provider.upper()}")

    def process_product_content(self, product_name, image_path, target_platforms):
        """
        ฟังก์ชันแปลงข้อมูลสินค้าให้เป็นสคริปต์วิดีโอ 4 ขั้นตอน (Hero -> Detail -> Usage -> Final Shot)
        และสร้างแคปชันตามแพลตฟอร์มเป้าหมาย
        
        :param product_name: ชื่อสินค้าหรือรายละเอียด
        :param image_path: พาธของรูปภาพสินค้า
        :param target_platforms: ลิสต์แพลตฟอร์มเป้าหมาย เช่น ['TikTok', 'Shopee', 'Facebook']
        """
        # 1. จัดทำโครงสร้างวิดีโอตามหลัก Product Storyboarding
        script_structure = self._build_video_script(product_name)

        # 2. เจนแคปชันแยกตามแพลตฟอร์มโดยอ้างอิง AI Engine ที่เลือก
        captions = {}
        for platform in target_platforms:
            captions[platform] = self._generate_caption(product_name, platform)

        # 3. รวบรวมผลลัพธ์เพื่อส่งกลับหน้าเว็บ (Frontend)
        result = {
            "status": "success",
            "selected_ai": self.ai_provider,
            "product": product_name,
            "video_script": script_structure,
            "captions": captions
        }
        return result

    def _build_video_script(self, product_name):
        """
        สร้างสคริปต์วิดีโอแบ่งเป็น 4 ลำดับฉาก
        """
        return {
            "1_product_hero": f"เปิดตัวสินค้าให้น่าสนใจ: 'หยุดดูตรงนี้ก่อน! พบกับ {product_name}'",
            "2_detail": f"อธิบายจุดเด่น/สรรพคุณของ {product_name} อย่างกระชับ",
            "3_usage": f"สาธิตการใช้งานจริงให้เห็นผลลัพธ์ชัดเจน",
            "4_final_shot": f"กระตุ้นการตัดสินใจ: 'กดสั่งซื้อที่ตะกร้าเหลืองซ้ายมือได้เลย!'"
        }

    def _generate_caption(self, product_name, platform):
        """
        สร้างข้อความแคปชันขายของเฉพาะแพลตฟอร์ม
        """
        if self.ai_provider == "chatgpt":
            prefix = "[ChatGPT Output] "
        elif self.ai_provider == "gemini":
            prefix = "[Gemini Output] "
        else:
            prefix = "[Grok Output] "

        if platform.lower() == "tiktok":
            return f"{prefix}🔥 ป้ายยาแรงมาก! {product_name} ของมันต้องมี พิกัดในตะกร้าเลยจ้า #TikTokShop #คุณนายสายอีสาน"
        elif platform.lower() == "shopee":
            return f"{prefix}🛒 ช้อปด่วน {product_name} ลดราคาพิเศษ การันตีของแท้ กดใส่ตะกร้าเลย! #ShopeeTH"
        else:
            return f"{prefix}✨ รีวิว {product_name} ใช้แล้วชอบมาก สั่งซื้อ/สอบถามทักแชตได้เลยค่ะ #FacebookReels"


# --- ส่วนทดสอบการทำงานของโค้ด (Test Execution) ---
if __name__ == "__main__":
    # ทดสอบเรียกใช้ด้วย ChatGPT Engine
    engine = AutoGenXEngine(ai_provider="chatgpt")
    
    # จำลองการส่งข้อมูล
    output = engine.process_product_content(
        product_name="ทิชชู่ห่อหนาพิเศษ (ดึงจากข้างล่างห่อ)",
        image_path="sample_tissue.jpg",
        target_platforms=["TikTok", "Shopee", "Facebook"]
    )
    
    print("\n=== ผลลัพธ์ที่ได้จากระบบ ===")
    print(json.dumps(output, indent=4, ensure_ascii=False))
