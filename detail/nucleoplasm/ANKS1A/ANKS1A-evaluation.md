---
type: protein-evaluation
gene: "ANKS1A"
date: 2026-06-03
tags: [protein-scout, nucleoplasm, evaluation, full-reevaluate]
status: scored
---
## ANKS1A

Q92625 | Ankyrin repeat and SAM domain-containing protein 1A | ~1100aa (estimated from family) | AF not found | PM=21 | norm=60.7/100

| 维度 | 得分 | 权重 | 加权 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32 |
| 蛋白大小 | 8/10 | ×1 | 8 |
| 研究新颖性 | 8/10 | ×5 | 40 |
| 三维结构 | 0/10 | ×3 | 0 |
| 调控结构域 | 5/10 | ×2 | 10 |
| PPI 网络 | 7/10 | ×3 | 21 |
| **加权总分** | | | **111/180** |
| 互证加分 | | | +0.5 |
| **PubMed strict** | 21 | | |
| **归一化总分 (÷1.83)** | | | **60.7/100** |

**UniProt**: 数据获取失败（URLError: EOF occurred in violation of protocol）。UniProt accession Q92625 来自 HPA 数据，但抓取过程中 SSL 连接错误导致 UniProt 注释不可用。以下评估基于 HPA、STRING、IntAct 和 PubMed 数据。

**AlphaFold**: 未找到 AF 条目（AlphaFold DB 查询返回 found=false）。可能因为基因名/accession 映射问题或该蛋白未被 AlphaFold 收录。

**HPA IF 状态**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 核定位评定
HPA 主定位 Nucleoplasm (Approved)，额外定位 Cytosol。UniProt 数据不可用，无法获得 GO-CC 或 UniProt subcellular 注释的独立验证。HPA IF reliability 为 Approved 级别，Nucleoplasm 列为主定位，提供核定位的主要证据。因缺乏 Orthogonal 验证来源，评为 8/10（保守）。

### 蛋白大小
UniProt 未获取，无法精确确认长度和分子量。基于 ANKS1B (1248 aa, 138.1 kDa) 的家族参考，ANKS1A 约为 1100-1200 aa。Structurally an ANK repeat + SAM + PTB domain protein（从基因名和 STRING 互作模式推断）。评为 8/10（估计值）。

### 研究新颖性
PubMed strict count = 21（21-40 档）。关键研究：(1) PMID 38123547 (2023) — ANKS1A 调控 LRP1 介导的脑血管内皮细胞清除 (Nature Communications)；(2) PMID 33504787 (2021) — 多纤毛细胞中亚远端附件的分子动力学 (Nature Communications)；(3) PMID 38052491 (2023) — ANKS1A 缺失异常增加蛋白转运机器进入室管膜纤毛；(4) PMID 36717454 (2022) — 适配蛋白 Anks1a 调控乳腺癌细胞运动性；(5) PMID 27802842 (2016) — 缺陷 Anks1a 破坏受体酪氨酸激酶从内质网的输出。研究涉及纤毛生物学、受体转运、癌症细胞运动，有较高质量文献。评为 8/10。

### PDB 结构
PAE 图像暂无数据（AlphaFold 未收录该蛋白）。无 AlphaFold 预测，无实验 PDB 结构。为 15 个基因中唯一完全无结构信息的蛋白。评为 0/10。

### 调控结构域
基于基因名和家族特征推断：Ankyrin repeat + SAM domain (sterile alpha motif) + 可能含 PTB domain。SAM 结构域参与蛋白-蛋白和蛋白-RNA 互作，常见于信号转导支架蛋白。此推断基于 ANKS1B 结构域架构（ANK + SAM + PTB），ANKS1A 可能拥有类似架构。评为 5/10。

### PPI 网络
STRING: RIN1 (0.790, exp 0.773)、DAB2IP (0.771, exp 0.756)、EGFR (0.752, exp 0.702) 等 15 个伙伴，其中 RIN1/RAS 信号、DAB2IP/RAS-GAP 和 EGFR/RTK 均为实验验证互作。IntAct: YWHAG/YWAHZ/YWHAQ/YWHAB (14-3-3 家族 co-IP)、EGFR (ubiquitin reconstruction)、SHC1 (co-IP)、CD2AP (Y2H)、EPHA1 (Y2H)、RPN1 (cross-linking) 等 15 条记录。14-3-3 家族蛋白的大量 co-IP 互作提示 ANKS1A 可能受磷酸化依赖的 14-3-3 调控。评为 7/10。

### 关键文献
- PMID 38123547: ANKS1A regulates LRP1-mediated cerebrovascular clearance in brain endothelial cells (Nat Commun, 2023)
- PMID 33504787: Molecular dynamics of subdistal appendages in multi-ciliated cells (Nat Commun, 2021)
- PMID 27802842: Defective Anks1a disrupts export of RTKs from ER (BMB Rep, 2016)

### 人工复核建议
**重要提醒**：该蛋白的 UniProt 和 AlphaFold 数据均未能获取。这是 15 个基因中唯一双缺失的情况，评估可靠性受限制。建议：(1) 重新尝试 UniProt API 获取 Q92625 数据；(2) 在 AlphaFold DB 中通过 accession Q92625 手动搜索；(3) 14-3-3 蛋白家族互作（YWHAG/YWAHZ/YWHAQ/YWHAB）是潜在的调控机制入口。若结构数据补全后，该蛋白的 SAM + PTB 信号适配架构在纤毛生物学和受体转运中具有研究价值。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000064999-ANKS1A/subcellular

![](https://images.proteinatlas.org/36768/403_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/36768/403_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/36768/406_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/36768/406_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/36768/408_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/36768/408_B4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
