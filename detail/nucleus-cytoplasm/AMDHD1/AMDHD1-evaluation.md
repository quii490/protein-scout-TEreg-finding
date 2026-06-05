---
type: protein-evaluation
gene: "AMDHD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AMDHD1 核蛋白评估报告（重新评估）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AMDHD1 |
| 蛋白大小 | 426 aa / 46.7 kDa |
| UniProt ID | Q96NU7 |
| 蛋白全名 | Probable imidazolonepropionase |
| 子定位分类 | nucleus-cytoplasm |
| HPA IF 主定位 | Cytosol |
| HPA IF 附加定位 | Nucleoplasm, Plasma membrane |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | 24 | HPA主定位Cytosol，Nucleoplasm为附加；核定位不主导但有信号 |
| 蛋白大小 | 10/10 | ×1 | 10 | 426aa/46.7kDa，理想实验范围 |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | pLDDT=96.2, pct>90=91.8%；极高质量预测 |
| 调控结构域 | 4/10 | ×2 | 8 | IPR006680 Amidohydrolase；组氨酸代谢酶，无调控域 |
| PPI网络 | 2/10 | ×3 | 6 | FTCD/HAL/UROC1组氨酸代谢通络；IntAct仅2条 |
| **加权总分** | | | **125/180**** | |
| **归一化总分 (÷1.83)** | | | **68.3/100**** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Cytosol (main), Nucleoplasm (additional), Plasma membrane (additional) | Approved |
| UniProt | 无亚细胞定位注释 | |
| GO-CC | GO:0005829 (cytosol, TAS:Reactome) | |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

#### 3.2 蛋白大小评估

426 aa / 46.7 kDa。理想范围，适中大小。含完整金属依赖性水解酶催化域。**评分: 10/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 12 |
| PubMed symbol_only | 19 |
| 主要方向 | 组氨酸代谢、甲状腺激素靶基因、维生素D代谢 |

**评价**: PubMed 仅 12 篇，极度新颖。AMDHD1 功能仍标注为"probable imidazolonepropionase"。作为组氨酸降解途径酶，研究极少，主要出现在 GWAS 和表达谱中。**评分: 10/10** (≤20篇)。

**关键文献**:
1. Okada M et al. (2015). "Direct Activation of Amidohydrolase Domain-Containing 1 Gene by Thyroid Hormone Implicates a Role in the Formation of Adult Intestinal Stem Cells During Xenopus Metamorphosis." *Endocrinology*. PMID: 26086244 — 甲状腺激素直接调控，干细胞形成
2. Jiang H et al. (2023). "Identification of metabolic biomarkers associated with nonalcoholic fatty liver disease." *Lipids Health Dis*. PMID: 37697333
3. Zhang X et al. (2023). "Causality assessment of circulating Vitamin D level on venous thromboembolism." *Nutr Metab Cardiovasc Dis*. PMID: 37414665
4. Song Y et al. (2013). "Identification of novel tissue-specific genes by analysis of microarray databases." *PLoS One*. PMID: 23741331
5. Kuechler EC et al. (2021). "The role of 25-hydroxyvitamin-D3 and vitamin D receptor gene in human periodontal ligament fibroblasts." *BMC Oral Health*. PMID: 34362362

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 96.2 |
| pLDDT > 90 (Very High) | 91.8% |
| pLDDT 70-90 (High) | 7.5% |
| pLDDT 50-70 (Medium) | 0.5% |
| pLDDT < 50 (Low) | 0.2% |
| 有序区域 (pLDDT>70) | 99.3% |
| 实验结构 (PDB) | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR006680 (Amidohydrolase-related); IPR005920 (Imidazolonepropionase); IPR011059 (Metal-dependent hydrolase, composite domain); IPR032466 (Metal-dependent hydrolase) |
| Pfam | PF01979 (Amidohydro_1) |

AMDHD1 为金属依赖性酰胺水解酶超家族成员，催化组氨酸降解中咪唑酮丙酸的环水解。含 TIM 桶状折叠和双金属催化中心。虽为代谢酶，但受甲状腺激素直接转录调控 (Okada 2015)，暗示可能与发育信号交叉。**评分: 4/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (top 10):

| Partner | Score | 实验证据 | 功能 |
|---------|-------|---------|------|
| FTCD | 0.977 | 0 | 组氨酸代谢 |
| HAL | 0.969 | 0 | 组氨酸代谢 |
| UROC1 | 0.881 | 0 | 组氨酸代谢 |
| NT5E | 0.814 | 0 | 核苷酸代谢 |
| MTAP | 0.742 | 0 | 甲硫氨酸回收 |
| CYP2R1 | 0.74 | 0 | 维生素D代谢 |
| PNP | 0.719 | 0 | 嘌呤代谢 |
| SEC23A | 0.716 | 0 | COPII囊泡 |
| AOX1 | 0.688 | 0 | 氧化代谢 |
| CYP24A1 | 0.686 | 0 | 维生素D代谢 |

PPI 网络完全集中于代谢通路 (组氨酸、维生素D、核苷酸)。无实验验证互作。IntAct 仅 2 条: KLHL23 (co-IP) + SYT11 (co-IP)。PPI 网络极弱。**评分: 2/10**。

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5) — 69.4/100

**核心优势**:
1. 极度新颖 (12篇)
2. AlphaFold 极高质量 (pLDDT 96.2, 99.3% 有序)
3. 甲状腺激素直接靶基因，与发育信号关联
4. 理想蛋白大小

**风险/不确定性**:
1. HPA 主定位为 Cytosol，核定位仅为附加
2. 功能仍为"probable"
3. PPI 网络极弱
4. 无实验结构
5. 代谢酶功能与核调控关联弱

**下一步建议**:
- [ ] 验证甲状腺激素调控下 AMDHD1 的核定位变化
- [ ] 确定核内 AMDHD1 是否具有非酶功能
- [ ] 在干细胞模型中探索 AMDHD1 的发育功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96NU7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96NU7
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AMDHD1%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000139344-AMDHD1
- STRING: https://string-db.org (API, species=9606)
- IntAct: https://www.ebi.ac.uk/intact/

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000139344-AMDHD1/subcellular

![](https://images.proteinatlas.org/40149/1718_E10_13_cr5bbc950eca481_blue_red_green.jpg)
![](https://images.proteinatlas.org/40149/1718_E10_18_cr57f3dc35bef2f_blue_red_green.jpg)
![](https://images.proteinatlas.org/40149/1763_D5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/40149/1763_D5_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/40149/1823_B3_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/40149/1823_B3_33_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96NU7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
