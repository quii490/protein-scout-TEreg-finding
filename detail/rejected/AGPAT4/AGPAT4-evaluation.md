---
type: protein-evaluation
gene: "AGPAT4"
date: 2026-06-03
tags: [protein-scout, rejected]
status: rejected
rejection_reason: nuclear_score ≤ 3
---

## AGPAT4 核蛋白评估报告（重新评估）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AGPAT4 |
| 蛋白大小 | 378 aa / 44.0 kDa |
| UniProt ID | Q9NRZ5 |
| 蛋白全名 | 1-acyl-sn-glycerol-3-phosphate acyltransferase delta |
| HPA IF 主定位 | Golgi apparatus |
| HPA IF 附加定位 | Nucleoli, Vesicles |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-03 |
| 评估结果 | **REJECTED** (nuclear_score=3) |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA主定位Golgi apparatus，仅附加Nucleoli；UniProt定位ER膜/线粒体外膜 |
| 蛋白大小 | 8/10 | ×1 | 8 | 378aa/44.0kDa，较小但在可操作范围 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=26 (21-40→8) |
| 三维结构 | 9/10 | ×3 | 27 | pLDDT=94.0, pct>90=85.7%，极高质量预测 |
| 调控结构域 | 3/10 | ×2 | 6 | IPR002123 (acyltransferase) + IPR032098 (AGPAT4-like)，代谢酶无调控域 |
| PPI网络 | 3/10 | ×3 | 9 | STRING: AGPAT1-5同家族为主；IntAct几乎全为酵母双杂交，无实验验证PPI |
| **加权总分** | | | **102/180** | |
| **归一化总分 (÷1.8)** | | | **56.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Golgi apparatus (main), Nucleoli (additional), Vesicles (additional) | Approved |
| UniProt | Endoplasmic reticulum membrane; Mitochondrial outer membrane | ISS/IBA evidence |
| GO-CC | GO:0005789 (ER membrane, TAS), GO:0005741 (mito outer membrane, IBA), GO:0012505 (endomembrane system) | |

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。AGPAT4 的 HPA Approved 级别 IF 将 Golgi apparatus 列为主定位，Nucleoli 仅为附加定位。UniProt 注释为 ER 膜和线粒体外膜蛋白，功能上为参与磷脂酸合成的酰基转移酶。核定位信号很弱，仅作为附加的 Nucleoli 存在。**评分: 3/10**。

#### 3.2 蛋白大小评估

378 aa / 44.0 kDa。蛋白较小但处于正常范围。作为内质网膜整合蛋白，大小适度。**评分: 8/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 26 |
| PubMed symbol_only | 47 |
| 主要方向 | 磷脂代谢、子宫内膜异位症、肝癌靶向治疗 |

**评价**: PubMed 26 篇 (strict)，较为新颖。近期高影响力研究集中在肝癌中的 AGPAT4 共价抑制剂 (Ng KY et al., 2025, *Sci Transl Med*) 和子宫内膜异位症多组学研究。**评分: 8/10** (21-40篇)。

**关键文献**:
1. Ng KY et al. (2025). "AGPAT4 targeted covalent inhibitor potentiates targeted therapy to overcome cancer cell plasticity in hepatocellular carcinoma." *Sci Transl Med*. PMID: 40737432
2. Zhukovsky MA et al. (2019). "The Structure and Function of AGPAT4/LPAATδ." *Front Cell Dev Biol*. PMID: 31428612
3. Chen J et al. (2024). "Unraveling the significance of AGPAT4 for the pathogenesis of endometriosis via a multi-omics approach." *Hum Genet*. PMID: 38850428
4. Mardian EB et al. (2017). "Agpat4/Lpaatδ deficiency highlights the molecular heterogeneity of epididymal and perirenal white adipose depots." *J Lipid Res*. PMID: 28814640
5. Li Z et al. (2023). "The regulation of AGPAT4 on the growth and lenvatinib resistance of hepatocellular carcinoma." *Zhonghua Gan Zang Bing Za Zhi*. PMID: 37248980

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 94.0 |
| pLDDT > 90 (Very High) | 85.7% |
| pLDDT 70-90 (High) | 11.6% |
| pLDDT 50-70 (Medium) | 0.8% |
| pLDDT < 50 (Low) | 1.9% |
| 有序区域 (pLDDT>70) | 97.3% |
| 实验结构 (PDB) | 无 |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。AlphaFold 预测质量极高 (pLDDT 94.0)，97.3% 残基处于有序状态，提示蛋白折叠良好。无实验结构。**评分: 9/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR002123 (Phospholipid/glycerol acyltransferase); IPR032098 (AGPAT4-like domain) |
| Pfam | PF01553 (Acyltransferase); PF16076 (AGPAT4 C-terminal) |

AGPAT4 为酰基转移酶家族成员，含两个特征性结构域。功能为催化溶血磷脂酸 (LPA) 向磷脂酸 (PA) 的转化，属于脂质代谢酶类，无已知的转录调控或染色质相互作用结构域。**评分: 3/10**。

#### 3.6 PPI 网络

STRING 互作以 AGPAT1-5 同家族蛋白为主 (score >0.9)，均为数据库/文本挖掘来源。IntAct 记录中多数为果蝇酵母双杂交 (p53, RpS24 等)，少数为人类 pull-down (UNC93B1) 和 co-IP (SH2D3C, VIPR1)。PPI 网络缺乏核蛋白互作和调控相关伙伴。**评分: 3/10**。

### 4. 拒绝理由

AGPAT4 nuclear_score=3 (≤3 阈值)，核心原因：
- HPA IF 主定位为 **Golgi apparatus**（高尔基体），非细胞核
- Nucleoli 仅作为附加定位出现
- UniProt 注释为 ER 膜和线粒体外膜蛋白
- 功能为酰基转移酶，参与磷脂代谢，无核定位信号或核功能证据

**结论**: 虽 PubMed 新颖度好、AlphaFold 质量极高，但核定位证据严重不足，不符合核蛋白筛选标准。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NRZ5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NRZ5
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AGPAT4%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000026652-AGPAT4
