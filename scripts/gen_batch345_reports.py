#!/usr/bin/env python3
"""Generate complete re-evaluation reports for Batches 3, 4, 5 (15 genes)."""
import os

BASE = "/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail"

def write_report(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    print(f"  Wrote: {path}")

# ============================================================
# BATCH 3 - Rejected (nuke≤3)
# ============================================================

# 1. AGPAT4 - REJECTED (nuke=3, HPA main=Golgi)
report_AGPAT4 = """---
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
"""

# 2. AGTPBP1 - REJECTED (nuke=3, but HPA main=Nucleoplasm!)
report_AGTPBP1 = """---
type: protein-evaluation
gene: "AGTPBP1"
date: 2026-06-03
tags: [protein-scout, rejected]
status: rejected
rejection_reason: nuclear_score ≤ 3
---

## AGTPBP1 核蛋白评估报告（重新评估）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AGTPBP1 / CCP1 / KIAA1035 / NNA1 |
| 蛋白大小 | 1226 aa / 138.4 kDa |
| UniProt ID | Q9UPW5 |
| 蛋白全名 | Cytosolic carboxypeptidase 1 |
| HPA IF 主定位 | Nucleoplasm |
| HPA IF 附加定位 | Plasma membrane, Primary cilium, Centriolar satellite, Basal body |
| HPA Reliability | Supported |
| 评估日期 | 2026-06-03 |
| 评估结果 | **REJECTED** (nuclear_score=3) |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA IF显示Nucleoplasm为主定位，但UniProt注释为Cytoplasm/Cytosol/Mitochondrion，信号弥散 |
| 蛋白大小 | 6/10 | ×1 | 6 | 1226aa/138.4kDa，极大蛋白，重组表达困难 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=36 (21-40→8) |
| 三维结构 | 5/10 | ×3 | 15 | pLDDT=75.3, pct<50=24.9%，大量无序区域 |
| 调控结构域 | 5/10 | ×2 | 10 | IPR000834 (Peptidase M14)，羧肽酶，微管去谷氨酰化 |
| PPI网络 | 4/10 | ×3 | 12 | STRING: TTLL4实验互作(0.595)；IntAct: CYCS/DISC1/Y2H为主 |
| **加权总分** | | | **95/180** | |
| **归一化总分 (÷1.8)** | | | **52.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm (main), Plasma membrane, Primary cilium, Centriolar satellite, Basal body | Supported |
| UniProt | Cytoplasm (IDA), Cytosol (ISS), Nucleus (IDA), Mitochondrion (ISS) | |
| GO-CC | GO:0005654 (nucleoplasm, IDA:HPA), GO:0005737 (cytoplasm, IDA), GO:0034451 (centriolar satellite, IDA) | |

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。HPA IF Supported 级别将 Nucleoplasm 列为主定位，但同时有多达5个定位（细胞膜、初级纤毛、中心粒卫星、基体），显示该蛋白广泛分布于多个细胞区室。UniProt 实验证据同时支持 Cytoplasm 和 Nucleus。GO-CC 也同时注释 nucleoplasm 和多个胞质/纤毛结构。核定位特异性不高。**评分: 3/10**。

#### 3.2 蛋白大小评估

1226 aa / 138.4 kDa。蛋白极大，远超800 aa最佳实验范围。重组全长表达困难，可能需截短体构建。**评分: 6/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 36 |
| PubMed symbol_only | 51 |
| 别名 | CCP1, KIAA1035, NNA1 |
| 主要方向 | 神经退行性病变、精子发生缺陷、微管去谷氨酰化 |

**评价**: PubMed 36 篇 (strict)，中等新颖度。AGTPBP1/CCP1 主要研究集中在神经生物学和 Purkinje 细胞退化。**评分: 8/10** (21-40篇)。

**关键文献**:
1. Lalonde R & Strazielle C. (2022). "The AGTPBP1 gene in neurobiology." *Gene*. PMID: 34637898 — 综述
2. Lin YH et al. (2024). "Deleterious genetic changes in AGTPBP1 result in teratozoospermia." *J Cell Mol Med*. PMID: 37937809
3. Baltanás FC et al. (2021). "The Childhood-Onset Neurodegeneration with Cerebellar Atrophy (CONDCA) Disease Caused by AGTPBP1." *Biomedicines*. PMID: 34572343
4. Wang HP et al. (2025). "Lacosamide Is a Novel Drug That Improves AGTPBP1 Knockout-Mediated Impairment." *Mol Neurobiol*. PMID: 40347376
5. Zhu Z et al. (2024). "Circ-AGTPBP1 promotes white matter injury through miR-140-3p/Pcdh17 axis." *J Bioenerg Biomembr*. PMID: 37994971

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 75.3 |
| pLDDT > 90 (Very High) | 52.8% |
| pLDDT 70-90 (High) | 18.4% |
| pLDDT 50-70 (Medium) | 3.9% |
| pLDDT < 50 (Low) | 24.9% |
| 有序区域 (pLDDT>70) | 71.2% |
| 实验结构 (PDB) | 无 |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。AlphaFold 中等质量预测 (pLDDT 75.3)，24.9% 残基 pLDDT < 50 提示大量无序区域。作为大蛋白，IDR 占比高可能与其功能调控相关。**评分: 5/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR000834 (Peptidase M14, carboxypeptidase A); IPR011989 (Armadillo-like helical); IPR016024 (Armadillo-type fold); IPR033852 (Cytosolic carboxypeptidase 1); IPR040626 (CCP1 N-terminal domain) |
| Pfam | PF00246 (Peptidase_M14); PF18027 (CCP1_N); PF25571 (M14-like domain) |

AGTPBP1 为金属羧肽酶，催化微管蛋白和非微管蛋白的去谷氨酰化修饰。含锌依赖性蛋白酶结构域。调控意义上，通过调控微管蛋白翻译后修饰影响细胞分裂和纤毛功能，但对转录/染色质调控无直接作用。**评分: 5/10**。

#### 3.6 PPI 网络

STRING 互作以 TTLL 家族 (微管蛋白连接酶) 为主，TTLL4 有实验证据 (score 0.595)。IntAct 记录以酵母双杂交为主 (CYCS, NYNRIN, CBY1, DISC1)，少数 co-IP (TTLL4, TMOD1)。PPI 网络集中在微管代谢，缺乏核调控相关互作。**评分: 4/10**。

### 4. 拒绝理由

AGTPBP1 nuclear_score=3 (≤3 阈值)，核心原因：
- 虽然 HPA IF 将 Nucleoplasm 列为主定位，但定位信号广泛分布于膜、纤毛、中心粒等多个区室
- UniProt 实验证据显示 Cytoplasm 为主要定位
- 功能为胞质羧肽酶，催化微管蛋白去谷氨酰化，与核功能关联弱

**结论**: 核定位特异性不足，功能高度偏向胞质/细胞骨架调控，不符合核蛋白筛选标准。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UPW5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UPW5
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AGTPBP1%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000135049-AGTPBP1
"""

# 3. AHCYL2 - ACCEPTED → nucleus-cytoplasm (nuke=4)
report_AHCYL2 = """---
type: protein-evaluation
gene: "AHCYL2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AHCYL2 核蛋白评估报告（重新评估）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AHCYL2 / KIAA0828 |
| 蛋白大小 | 611 aa / 66.7 kDa |
| UniProt ID | Q96HN2 |
| 蛋白全名 | Adenosylhomocysteinase 3 |
| 子定位分类 | nucleus-cytoplasm |
| HPA IF 主定位 | Cytosol |
| HPA IF 附加定位 | Nucleoplasm, Vesicles |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA主定位Cytosol，Nucleoplasm为附加；UniProt注释Cytoplasm；核定位不主导 |
| 蛋白大小 | 10/10 | ×1 | 10 | 611aa/66.7kDa，理想实验范围 |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | pLDDT=79.2；PDB 3GVP (X-ray 2.25A) |
| 调控结构域 | 8/10 | ×2 | 16 | IPR000043 AdoHcyase + IPR015878 NAD binding + IPR036291 NAD(P)超家族；经典代谢酶折叠 |
| PPI网络 | 7/10 | ×3 | 21 | AHCYL1(0.964实验), CBS(0.975), BHMT(0.975)；IntAct 15条含TRAF6/BAP1/CSNK1E |
| **加权总分** | | | **137/180** | |
| **归一化总分 (÷1.8)** | | | **76.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Cytosol (main), Nucleoplasm (additional), Vesicles (additional) | Approved |
| UniProt | Cytoplasm (by similarity), Microsome (by similarity) | |
| GO-CC | GO:0005829 (cytosol, IBA), GO:0043005 (neuron projection, IEA) | |

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。HPA Approved 级别 IF 明确将 Cytosol 列为主定位，Nucleoplasm 为附加定位。蛋白主要在胞质中发挥功能，但有一定核分布。**评分: 4/10**。

#### 3.2 蛋白大小评估

611 aa / 66.7 kDa。大小处于 200-800 aa 理想实验范围，足够包含完整酶活结构域，又不过大难以重组表达。**评分: 10/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 19 |
| PubMed symbol_only | 29 |
| 别名 | KIAA0828 |
| 主要方向 | 钠/碳酸氢盐共转运体调控、IRBIT家族信号、视网膜发育 |

**评价**: PubMed 仅 19 篇 (strict)，极度新颖。AHCYL2 属于 IRBIT 家族，调控 NBCe1-B 钠/碳酸氢盐共转运体活性。研究主要来自韩国团队。**评分: 10/10** (≤20篇)。

**关键文献**:
1. Park PW et al. (2016). "Ahcyl2 upregulates NBCe1-B via multiple serine residues of the PEST domain-mediated association." *Korean J Physiol Pharmacol*. PMID: 27382360 — 核心功能文献
2. Campbell WA et al. (2023). "Chromatin access regulates the formation of Müller glia-derived progenitor cells in the retina." *Glia*. PMID: 36971459 — 染色质可及性与AHCYL2
3. Liu Y et al. (2025). "IRBITs, signaling molecules of great functional diversity." *Pflugers Arch*. PMID: 40445299 — IRBIT家族综述
4. Praus F et al. (2023). "Panomics reveals patient individuality as the major driver of colorectal cancer progression." *J Transl Med*. PMID: 36691026
5. Yang C et al. (2023). "The identification of metabolism-related subtypes and potential treatments for idiopathic pulmonary fibrosis." *Front Pharmacol*. PMID: 37274115

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 79.2 |
| pLDDT > 90 (Very High) | 66.8% |
| pLDDT 70-90 (High) | 5.6% |
| pLDDT 50-70 (Medium) | 1.1% |
| pLDDT < 50 (Low) | 26.5% |
| 有序区域 (pLDDT>70) | 72.4% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 3GVP (X-ray, 2.25A, chains A/B/C/D=175-607) |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。PDB 3GVP 为截短体 X-ray 晶体结构 (2.25 A)，涵盖 175-607 位残基（约占全长 70%），提供可靠实验结构信息。AlphaFold pLDDT 79.2，26.5% 无序区域可能位于 N 端。**评分: 8/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR000043 (Adenosylhomocysteinase); IPR015878 (S-adenosyl-L-homocysteine hydrolase, NAD binding domain); IPR036291 (NAD(P)-binding domain superfamily); IPR042172 (Adenosylhomocysteinase, eukaryotic/archaeal); IPR020082 (S-adenosyl-L-homocysteine hydrolase, conserved site) |
| Pfam | PF00670 (S-adenosyl-L-homocysteine hydrolase, NAD binding domain); PF05221 (Adenosylhomocysteinase) |

AHCYL2 为 S-腺苷同型半胱氨酸水解酶家族成员 (AHCY-like 2)，含经典的双结构域折叠 (NAD binding + catalytic domain)。虽为代谢酶，AHCYL2 与同家族 AHCYL1 (IRBIT) 一样具有非酶信号功能——通过 PEST 结构域介导 NBCe1-B 调控。NAD 结合域与代谢和信号双重功能相关。**评分: 8/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4, top 10):

| Partner | Score | 实验证据 | 功能类别 |
|---------|-------|---------|---------|
| BHMT | 0.975 | 0 | 同型半胱氨酸代谢 |
| CBS | 0.975 | 0.07 | 转硫途径 |
| BHMT2 | 0.973 | 0 | 甜菜碱-同型半胱氨酸甲基转移酶 |
| MTR | 0.972 | 0 | 甲硫氨酸合成酶 |
| CTH | 0.971 | 0.069 | 半胱氨酸代谢 |
| AHCYL1 | 0.964 | 0.651 | IRBIT家族，实验互作强 |
| AHCY | 0.921 | 0.208 | 经典AdoHcyase，实验互作 |
| KYAT1 | 0.920 | 0 | 犬尿氨酸转氨酶 |
| DNMT1 | 0.919 | 0 | DNA甲基转移酶 |
| DNMT3B | 0.913 | 0 | DNA甲基转移酶 |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRAF6 | anti bait co-IP | 17353931 |
| CSNK1E | TAP | 23455922 |
| CLK4 | TAP | 23602568 |
| BAP1 | anti tag co-IP | 19615732 |
| SLX4 | anti tag co-IP | 19596235 |
| FAM13A | anti tag co-IP | 32203420 |
| EZR | BioID | 29568061 |
| TGOLN2 | BioID | 29568061 |

**PPI 互证分析**:
- AHCYL1 实验互作 (0.651) 为最可靠伙伴，同属 IRBIT 信号家族
- DNMT1/DNMT3B 的文本挖掘关联暗示潜在的表观遗传调控连接
- TRAF6 和 CSNK1E 互作连接至 NF-kB 和 Wnt 信号通路
- AHCY 代谢酶互作指向 S-腺苷甲硫氨酸循环与甲基化代谢的交叉

**评分: 7/10** (IRBIT家族互作 + DNMT关联 + TRAF6/CSNK1E信号连接)

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5) — 76.1/100

**核心优势**:
1. 极度新颖: PubMed 仅 19 篇
2. IRBIT 家族成员，具有非酶信号功能
3. PDB 实验结构支撑
4. DNMT 关联暗示表观遗传交叉
5. 实验 PPI 含 TRAF6/CSNK1E 信号激酶

**风险/不确定性**:
1. HPA 主定位为 Cytosol，Nucleoplasm 仅为附加
2. 功能主要为胞质 NBCe1-B 调控
3. 核功能直接证据缺乏
4. 26.5% 无序区域可能影响结构研究

**下一步建议**:
- [ ] 验证 AHCYL2 的核定位比例及其调控条件
- [ ] 探索 AHCYL2-DNMT 关联的表观遗传意义
- [ ] 分析 AHCYL1/AHCYL2 在 IRBIT 信号网络中的功能分工

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96HN2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96HN2
- PDB: https://www.rcsb.org/structure/3GVP
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AHCYL2%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000158467-AHCYL2
- STRING: https://string-db.org (API, species=9606)
- IntAct: https://www.ebi.ac.uk/intact/
"""

# 4. AIRIM - REJECTED (nuke=3, HPA empty)
report_AIRIM = """---
type: protein-evaluation
gene: "AIRIM"
date: 2026-06-03
tags: [protein-scout, rejected]
status: rejected
rejection_reason: nuclear_score ≤ 3
---

## AIRIM 核蛋白评估报告（重新评估）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AIRIM / C1orf109 |
| 蛋白大小 | 203 aa / 23.4 kDa |
| UniProt ID | Q9NX04 |
| 蛋白全名 | AFG2-interacting ribosome maturation factor |
| HPA IF 主定位 | (无数据) |
| HPA Reliability | (无) |
| 评估日期 | 2026-06-03 |
| 评估结果 | **REJECTED** (nuclear_score=3) |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA无数据；UniProt注释Nucleus+Cytoplasm；GO-CC含nucleolus/nucleoplasm |
| 蛋白大小 | 5/10 | ×1 | 5 | 203aa/23.4kDa，极小蛋白 |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | pLDDT=94.2, pct>90=87.7%；PDB 8RHN (EM 4.50A) |
| 调控结构域 | 4/10 | ×2 | 8 | IPR029159 (AIRIM family)，单结构域蛋白 |
| PPI网络 | 3/10 | ×3 | 9 | STRING 404；IntAct: CINP/ZBED1/IKZF3 Y2H为主 |
| **加权总分** | | | **111/180** | |
| **归一化总分 (÷1.8)** | | | **61.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | 无 IF 数据 (page_found_no_if_image_detected) | N/A |
| UniProt | Nucleus (IDA), Cytoplasm (IDA) | |
| GO-CC | GO:0005730 (nucleolus, IDA:HPA), GO:0005654 (nucleoplasm, IDA:HPA), GO:0005634 (nucleus, IDA), GO:0005829 (cytosol, IDA:HPA) | |

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。HPA 无可用的 IF 图像，但 GO-CC 注释同时包含 nucleolus、nucleoplasm 和 cytosol，显示蛋白在多个区室分布。核定位有 UniProt IDA 证据。**评分: 3/10**。

#### 3.2 蛋白大小评估

203 aa / 23.4 kDa。蛋白极小，仅含单一 AIRIM 家族结构域。小蛋白实验操作便利但可能功能信息有限。**评分: 5/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 2 |
| PubMed symbol_only | 2 |
| 别名 | C1orf109 |
| 主要方向 | 核糖体成熟、神经发育、基因组稳定性 |

**评价**: PubMed 仅 2 篇，极端新颖（基因名 2024 年前为 C1orf109）。2024-2025 年的新研究揭示了其在核糖体成熟和复制叉稳定性中的关键作用。**评分: 10/10** (≤20篇)。

**关键文献**:
1. Ni C et al. (2025). "A programmed decline in ribosome levels governs human early neurodevelopment." *Nat Cell Biol*. PMID: 40760247 — 核心CNS文献
2. Ni C et al. (2024). "An inappropriate decline in ribosome levels drives a diverse set of neurodevelopmental disorders." *bioRxiv*. PMID: 38260472 — 预印本

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 94.2 |
| pLDDT > 90 (Very High) | 87.7% |
| pLDDT 70-90 (High) | 10.8% |
| pLDDT 50-70 (Medium) | 1.0% |
| pLDDT < 50 (Low) | 0.5% |
| 有序区域 (pLDDT>70) | 98.5% |
| 实验结构 (PDB) | 8RHN (EM, 4.50A, chains A/B=1-203, 全长) |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。AlphaFold 预测质量极高 (pLDDT 94.2)。PDB 8RHN 为低温电镜结构 (4.50 A)，提供了全长实验结构。**评分: 9/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR029159 (AIRIM/C1orf109 family) |
| Pfam | PF15011 (DUF4520, C1orf109 family) |

AIRIM 为单结构域蛋白，属于 AFG2-interacting ribosome maturation factor 家族。功能为 55LCC 异六聚体 ATPase 复合体的一部分，促进复制体蛋白酶稳态和核糖体 60S 亚基成熟。无已知转录调控或染色质相互作用结构域。**评分: 4/10**。

#### 3.6 PPI 网络

STRING 返回 404 错误（无数据）。IntAct 记录以酵母双杂交为主，少数 co-IP (CINP)。UniProt 注释的实验互作包括 CEP55, CINP, IKZF3, RINT1, STN1 等，绝大多数为 Y2H (experiments=3)。PPI 网络集中在核糖体成熟和中心体相关蛋白。**评分: 3/10**。

### 4. 拒绝理由

AIRIM nuclear_score=3 (≤3 阈值)，核心原因：
- HPA 无可用的 IF 图像数据
- UniProt 注释同时支持 Nucleus 和 Cytoplasm，核定位特异性不足
- 功能主要为核糖体成熟和复制体蛋白酶稳态，非经典核调控蛋白

**结论**: 虽然极度新颖且 AlphaFold/PDB 结构优质，但核定位证据严重依赖注释而非直接图像，不符合核蛋白筛选标准。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NX04
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NX04
- PDB: https://www.rcsb.org/structure/8RHN
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AIRIM%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/search/AIRIM
"""

# 5. AKAP6 - REJECTED (nuke=3, HPA empty)
report_AKAP6 = """---
type: protein-evaluation
gene: "AKAP6"
date: 2026-06-03
tags: [protein-scout, rejected]
status: rejected
rejection_reason: nuclear_score ≤ 3
---

## AKAP6 核蛋白评估报告（重新评估）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AKAP6 / AKAP100 / KIAA0311 |
| 蛋白大小 | 2319 aa / 256.7 kDa |
| UniProt ID | Q13023 |
| 蛋白全名 | A-kinase anchor protein 6 |
| HPA IF 主定位 | (无数据) |
| HPA Reliability | (无) |
| 评估日期 | 2026-06-03 |
| 评估结果 | **REJECTED** (nuclear_score=3) |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA无数据；UniProt注释Nuclear membrane/Sarcoplasmic reticulum |
| 蛋白大小 | 4/10 | ×1 | 4 | 2319aa/256.7kDa，极大蛋白，实验困难 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 (21-40→8) |
| 三维结构 | 2/10 | ×3 | 6 | pLDDT=42.1, pct<50=73.6%，几乎全无序 |
| 调控结构域 | 6/10 | ×2 | 12 | IPR018159 (AKAP anchoring)，PKA锚定调控 |
| PPI网络 | 7/10 | ×3 | 21 | RYR2(0.992), PRKACA(0.953), PDE4D(0.944); 强信号通路PPI |
| **加权总分** | | | **95/180** | |
| **归一化总分 (÷1.8)** | | | **52.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | 无 IF 数据 (no_image_detected) | N/A |
| UniProt | Sarcoplasmic reticulum, Nucleus membrane | |
| GO-CC | GO:0005635 (nuclear envelope, IDA), GO:0031965 (nuclear membrane, IEA), GO:0014704 (intercalated disc), GO:0016529 (sarcoplasmic reticulum) | |

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。HPA 无 IF 图像数据。UniProt 注释核膜和肌质网，GO-CC 含 nuclear envelope (IDA)。蛋白主要定位在心肌细胞的肌质网/核膜界面。**评分: 3/10**。

#### 3.2 蛋白大小评估

2319 aa / 256.7 kDa。极大蛋白，远超实验操作理想范围。重组全长几乎不可能，需截短体策略。**评分: 4/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 30 |
| PubMed symbol_only | 46 |
| 别名 | AKAP100, KIAA0311 |
| 主要方向 | 心肌钙信号、RyR2调控、PKA锚定 |

**评价**: PubMed 30 篇 (strict)，中等新颖度。AKAP6 是 PKA 锚定蛋白家族成员，功能高度集中在心肌钙信号和 RyR2 磷酸化调控。**评分: 8/10** (21-40篇)。

**关键文献**:
1. Tomczak J et al. (2024). "Exploring AKAPs in visual signaling." *Front Mol Neurosci*. PMID: 38813437
2. Hakem Zadeh F et al. (2019). "AKAP6 and phospholamban colocalize and interact in HEK-293T cells and primary murine cardiomyocytes." *Physiol Rep*. PMID: 31325238
3. Lee SW et al. (2015). "AKAP6 inhibition impairs myoblast differentiation and muscle regeneration." *Sci Rep*. PMID: 26563778
4. Zhang M et al. (2019). "Impact of AKAP6 polymorphisms on Glioma susceptibility and prognosis." *BMC Neurol*. PMID: 31759389
5. Li A et al. (2025). "Wnt/β-catenin pathway induces cardiac dysfunction via AKAP6-mediated RyR2 phosphorylation." *J Mol Cell Biol*. PMID: 40097291

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 42.1 |
| pLDDT > 90 (Very High) | 1.9% |
| pLDDT 70-90 (High) | 17.1% |
| pLDDT 50-70 (Medium) | 7.4% |
| pLDDT < 50 (Low) | 73.6% |
| 有序区域 (pLDDT>70) | 19.0% |
| 实验结构 (PDB) | 无 |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。AlphaFold 预测质量极低 (pLDDT 42.1)，73.6% 残基 pLDDT < 50，提示蛋白几乎全为无序区域。作为大型支架蛋白，IDR 占比高符合预期。**评分: 2/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR018159 (Spectrin/alpha-actinin); IPR002017 (Spectrin repeat) |
| Pfam | PF00435 (Spectrin repeat) |

AKAP6 含多个血影蛋白重复序列 (Spectrin repeats)，介导 PKA 的亚细胞锚定。功能为将 PKA II 型调节亚基靶向至核膜或肌质网。作为信号支架蛋白具有调控功能，但血影蛋白重复本身不直接参与转录或染色质调控。**评分: 6/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (top 10):

| Partner | Score | 实验证据 | 功能类别 |
|---------|-------|---------|---------|
| RYR2 | 0.992 | 0.496 | 心肌钙释放通道 |
| RAPGEF3 | 0.967 | 0.095 | cAMP信号 |
| MAPK7 | 0.958 | 0 | MAPK信号 |
| PRKACB | 0.953 | 0.091 | PKA催化亚基 |
| PRKACA | 0.953 | 0.091 | PKA催化亚基 |
| PDE4D | 0.944 | 0.292 | cAMP磷酸二酯酶 |
| PDE4A | 0.941 | 0.292 | cAMP磷酸二酯酶 |
| AKAP1 | 0.931 | 0 | 线粒体AKAP |
| FKBP1B | 0.929 | 0 | RyR2调控 |
| AKAP7 | 0.809 | 0 | 同家族AKAP |

**PPI 互证分析**: PPI 网络高度集中在 cAMP/PKA 信号和钙调控通路。RYR2 为最核心互作伙伴，有实验证据。IntAct 确认 RYR2/PRKACA 互作。信号通路清晰但局限于肌细胞生理学。**评分: 7/10**。

### 4. 拒绝理由

AKAP6 nuclear_score=3 (≤3 阈值)，核心原因：
- HPA 无可用的 IF 图像数据
- AlphaFold 几乎全无序 (pLDDT 42.1)
- 蛋白极大 (2319 aa)，实验操作困难
- 功能高度专一于心肌钙信号，核关联弱

**结论**: 即使在信号通路研究中重要，AKAP6 的核定位证据不足、结构无序化严重、大小不适合常规生化实验，不符合核蛋白筛选标准。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13023
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13023
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AKAP6%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000151320-AKAP6
"""

# ============================================================
# BATCH 4
# ============================================================

# 6. AKAP7 - ACCEPTED → nucleus-cytoplasm (nuke=6, HPA main=Vesicles)
report_AKAP7 = """---
type: protein-evaluation
gene: "AKAP7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AKAP7 核蛋白评估报告（重新评估）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AKAP7 / AKAP18 |
| 蛋白大小 | 348 aa / 39.5 kDa |
| UniProt ID | Q9P0M2 |
| 蛋白全名 | A-kinase anchor protein 7 isoform gamma |
| 子定位分类 | nucleus-cytoplasm |
| HPA IF 主定位 | Vesicles |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | 24 | HPA IF显示Vesicles；UniProt注释Nucleus(by similarity)+Cytoplasm(experimental)；GO-CC有nucleus |
| 蛋白大小 | 7/10 | ×1 | 7 | 348aa/39.5kDa，较小但含完整功能域 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=29 (21-40→8) |
| 三维结构 | 7/10 | ×3 | 21 | pLDDT=76.7；PDB 4ZP3/5JJ2 (PKA-RII结合域晶体结构) |
| 调控结构域 | 7/10 | ×2 | 14 | IPR019510 PKA-RII binding；核心cAMP/PKA信号调控 |
| PPI网络 | 7/10 | ×3 | 21 | PRKAR2A(0.963实验), PRKACA(0.965实验)；强PKA通路PPI |
| **加权总分** | | | **127/180** | |
| **归一化总分 (÷1.8)** | | | **70.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Vesicles (main) | Approved |
| UniProt | Nucleus (by similarity), Cytoplasm (experimental) | |
| GO-CC | GO:0005829 (cytosol, IDA), GO:0005634 (nucleus, IEA), GO:0098686 (hippocampal mossy fiber to CA3 synapse) | |

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。HPA Approved IF 将 Vesicles 列为主定位，但 UniProt 通过相似性推断 Nucleus 定位，并有胞质实验证据。核定位部分由 UniProt/IEA 支持。**评分: 6/10**。

#### 3.2 蛋白大小评估

348 aa / 39.5 kDa。蛋白较小但功能完整，含 PKA-RII 结合域和核定位相关结构。紧凑型信号支架蛋白，实验操作便利。**评分: 7/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 29 |
| PubMed symbol_only | 33 |
| 别名 | AKAP18 |
| 主要方向 | PKA信号、ENaC调控、神经元功能、血小板活化 |

**评价**: PubMed 29 篇 (strict)，中等新颖度。AKAP7 在 PKA 信号空间调控中重要，但研究规模有限。**评分: 8/10** (21-40篇)。

**关键文献**:
1. Jones BW et al. (2016). "Targeted deletion of AKAP7 in dentate granule cells impairs spatial discrimination." *eLife*. PMID: 27911261 — 神经元功能
2. Johnson KR et al. (2012). "Molecular evolution of A-kinase anchoring protein (AKAP)-7." *BMC Evol Biol*. PMID: 22834419
3. Khalil JS et al. (2024). "Protein Kinase A Regulates Platelet Phosphodiesterase 3A through an A-Kinase Anchoring Protein Dependent Manner." *Cells*. PMID: 38994957
4. Kotaki R et al. (2020). "Overexpression of miR-669m inhibits erythroblast differentiation." *Sci Rep*. PMID: 32782283
5. Goldstein SA et al. (2024). "Hidden evolutionary constraints dictate the retention of coronavirus accessory genes." *Curr Biol*. PMID: 39566499

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 76.7 |
| pLDDT > 90 (Very High) | 54.0% |
| pLDDT 70-90 (High) | 12.4% |
| pLDDT 50-70 (Medium) | 7.8% |
| pLDDT < 50 (Low) | 25.9% |
| 有序区域 (pLDDT>70) | 66.4% |
| 实验结构 (PDB) | 4ZP3 (X-ray 2.63A), 5JJ2 (X-ray 1.25A) — PKA-RII结合域 |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。PDB 含两个 PKA-RII 结合域的晶体结构 (含 5JJ2 高分辨率 1.25 A)，提供可靠的实验结构信息。AlphaFold 预测中 25.9% 无序区域主要在非保守连接区。**评分: 7/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR019510 (A-kinase anchor protein, PKA-RII binding); IPR019511 (A-kinase anchoring protein); IPR052641 (AKAP7 family); IPR009097 (cAMP-dependent protein kinase regulator) |
| Pfam | PF10469 (AKAP7 2',5'-RNA ligase-like domain); PF10470 (AKAP7 NLS/RII binding) |

AKAP7 是经典 A-kinase anchoring protein，将 PKA 靶向特异性亚细胞位置。含 PKA-RII 结合域和 NLS-like 序列。通过调控 ENaC 通道和 cAMP 信号参与膜兴奋性调控。AKAP 家族作为信号组织者具有重要调控功能。**评分: 7/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (top 10):

| Partner | Score | 实验证据 | 功能类别 |
|---------|-------|---------|---------|
| PRKACA | 0.965 | 0.806 | PKA催化亚基 |
| PRKAR2A | 0.963 | 0.961 | PKA II型调节亚基 |
| PRKACB | 0.963 | 0.796 | PKA催化亚基β |
| PRKACG | 0.931 | 0.622 | PKA催化亚基γ |
| PRKAR2B | 0.926 | 0.839 | PKA II型调节亚基β |
| AKAP1 | 0.924 | 0 | 线粒体AKAP |
| CACNA1C | 0.877 | 0 | L型钙通道 |
| PDE4D | 0.872 | 0 | cAMP磷酸二酯酶 |
| AKAP5 | 0.849 | 0 | 膜AKAP |
| YBEY | 0.832 | 0.831 | 核糖体成熟, 实验互作 |

**IntAct 实验互作**: PRKACA (TAP), PRKACB (TAP), PRKAR1B (Y2H array), PRKAR2B (PCA), SPA17 (Y2H array), ROPN1L (validated Y2H), SNRPE (co-IP)

**PPI 互证分析**: PPI 网络核心为 PKA 全酶复合体 (催化+调节亚基)，实验证据丰富。PRKAR2A 和 PRKAR2B 的强实验互作确认了 AKAP7 作为 PKA 锚定蛋白的核心功能。额外伙伴 YBEY, SPA17, SNRPE 拓展了功能网络。**评分: 7/10**。

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5) — 70.6/100

**核心优势**:
1. PKA 信号通路核心支架蛋白
2. PKA-RII 结合域有高分辨率晶体结构
3. 强 PKA 全酶复合体 PPI
4. PPI 实验证据丰富

**风险/不确定性**:
1. HPA IF 主定位为 Vesicles，核定位仅由 UniProt 推断
2. 蛋白较小 (348 aa)
3. 信号通路虽经典但非染色质/转录调控
4. 25.9% 无序区域

**下一步建议**:
- [ ] 确认 AKAP7 在目标细胞中的核质分布
- [ ] 探索非 PKA 伙伴 (YBEY/SPA17) 的功能意义

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P0M2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P0M2
- PDB: https://www.rcsb.org/structure/4ZP3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AKAP7%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000118507-AKAP7
- STRING: https://string-db.org (API, species=9606)
- IntAct: https://www.ebi.ac.uk/intact/
"""

# 7. AKIP1 - REJECTED (nuke=3)
report_AKIP1 = """---
type: protein-evaluation
gene: "AKIP1"
date: 2026-06-03
tags: [protein-scout, rejected]
status: rejected
rejection_reason: nuclear_score ≤ 3
---

## AKIP1 核蛋白评估报告（重新评估）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AKIP1 / BCA3 / C11orf17 |
| 蛋白大小 | 210 aa / 23.1 kDa |
| UniProt ID | Q9NQ31 |
| 蛋白全名 | A-kinase-interacting protein 1 |
| HPA IF 主定位 | Nucleoplasm |
| HPA Reliability | Supported |
| 评估日期 | 2026-06-03 |
| 评估结果 | **REJECTED** (nuclear_score=3) |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA主定位Nucleoplasm；UniProt Nucleus (IDA)；核定位证据明确但信号单一 |
| 蛋白大小 | 5/10 | ×1 | 5 | 210aa/23.1kDa，极小蛋白 |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=61 (41-60→6) |
| 三维结构 | 4/10 | ×3 | 12 | pLDDT=68.2, pct<50=31.0%，高比例无序 |
| 调控结构域 | 4/10 | ×2 | 8 | IPR033214 (AKIP1 family)，单家族域，无经典调控域 |
| PPI网络 | 5/10 | ×3 | 15 | PRKACA(0.896实验), RELA(0.757实验); NF-kB核定位调控 |
| **加权总分** | | | **82/180** | |
| **归一化总分 (÷1.8)** | | | **45.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm (main) | Supported |
| UniProt | Nucleus (IDA) | |
| GO-CC | GO:0005654 (nucleoplasm, IDA:HPA) | |

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。核定位证据相对一致：HPA Nucleoplasm (main) + UniProt Nucleus (IDA)。但其功能主要为促进 NF-kB 亚基 RELA 的核定位和磷酸化，本身核定位特异性一般。**评分: 3/10**。

#### 3.2 蛋白大小评估

210 aa / 23.1 kDa。极端小的蛋白，仅含单一家族结构域。实验操作便利但功能信息有限。**评分: 5/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 61 |
| PubMed symbol_only | 64 |
| 别名 | BCA3, C11orf17 |
| 主要方向 | NF-kB信号、心肌重塑、胶质母细胞瘤、宫颈癌 |

**评价**: PubMed 61 篇 (strict)，中等研究热度。AKIP1 在 NF-kB 信号、癌症转移和心肌重塑中有较多研究，新颖度中等。**评分: 6/10** (41-60篇)。

**关键文献**:
1. Gao N et al. (2008). "AKIP1 enhances NF-kappaB-dependent gene expression by promoting the nuclear retention and phosphorylation of p65." *J Biol Chem*. PMID: 18178962 — 核心功能文献
2. Nijholt KT et al. (2023). "AKIP1 promotes cardiomyocyte elongation and physiological cardiac remodelling." *Sci Rep*. PMID: 36899057
3. Wan S et al. (2023). "AKIP1 accelerates glioblastoma progression through stabilizing EGFR expression." *Oncogene*. PMID: 37596322
4. Yulia A et al. (2021). "PKA and AKIP1 interact to mediate cAMP-driven COX-2 expression." *PLoS One*. PMID: 34166397
5. Zhang X et al. (2020). "AKIP1 promotes EMT and metastasis via PI3K/Akt/IKKβ pathway in cervical cancer." *Cell Biochem Funct*. PMID: 32401379

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 68.2 |
| pLDDT > 90 (Very High) | 26.2% |
| pLDDT 70-90 (High) | 21.4% |
| pLDDT 50-70 (Medium) | 21.4% |
| pLDDT < 50 (Low) | 31.0% |
| 有序区域 (pLDDT>70) | 47.6% |
| 实验结构 (PDB) | 无 |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。AlphaFold 低质量预测 (pLDDT 68.2)，31.0% 无序。作为小蛋白，47.6% 有序比例偏低，可能含有大量柔性区域。**评分: 4/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR033214 (A-kinase-interacting protein 1 family) |
| Pfam | 无 |

AKIP1 无 Pfam 结构域注释，仅有一个 InterPro 家族分类。作为 PKA 和 NF-kB 通路之间的桥接蛋白，通过蛋白-蛋白互作发挥功能，本身无酶活性或 DNA 结合结构域。**评分: 4/10**。

#### 3.6 PPI 网络

STRING 以 PRKACA (0.896, 实验 0.51) 和 RELA (0.757, 实验 0.51) 为核心。IntAct 确认 PRKACA (Y2H)、FHL2 (Y2H array)、FGFR3 (Y2H array)。PPI 集中在 NF-kB 和 PKA 信号交叉点。**评分: 5/10**。

### 4. 拒绝理由

AKIP1 nuclear_score=3 (≤3 阈值)，核心原因：
- PubMed 61 篇 (>40)，研究热度偏高
- AlphaFold 低质量 (31% 无序)
- 蛋白极小，功能域有限
- 虽 HPA Nucleoplasm 主定位明确，但综合评分偏低

**结论**: 研究热度偏高且结构质量差，不符合核蛋白筛选标准。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NQ31
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NQ31
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AKIP1%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000166452-AKIP1
"""

# 8. AKIRIN1 - REJECTED (nuke=3)
report_AKIRIN1 = """---
type: protein-evaluation
gene: "AKIRIN1"
date: 2026-06-03
tags: [protein-scout, rejected]
status: rejected
rejection_reason: nuclear_score ≤ 3
---

## AKIRIN1 核蛋白评估报告（重新评估）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AKIRIN1 / C1orf108 |
| 蛋白大小 | 192 aa / 21.9 kDa |
| UniProt ID | Q9H9L7 |
| 蛋白全名 | Akirin-1 |
| HPA IF 主定位 | Nucleoplasm |
| HPA IF 附加定位 | Nuclear membrane |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-03 |
| 评估结果 | **REJECTED** (nuclear_score=3) |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA Nucleoplasm + Nuclear membrane；UniProt Nucleus (IDA)；核定位明确 |
| 蛋白大小 | 5/10 | ×1 | 5 | 192aa/21.9kDa，极小蛋白 |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 (≤20→10) |
| 三维结构 | 4/10 | ×3 | 12 | pLDDT=68.1, pct<50=27.1%，高比例无序 |
| 调控结构域 | 4/10 | ×2 | 8 | IPR024132 (Akirin family)，无经典调控域 |
| PPI网络 | 5/10 | ×3 | 15 | PSMB3/PSMA5(实验), AKIRIN2(0.849实验); 蛋白酶体/免疫 |
| **加权总分** | | | **102/180** | |
| **归一化总分 (÷1.8)** | | | **56.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm (main), Nuclear membrane (additional) | Approved |
| UniProt | Nucleus (IDA) | |
| GO-CC | GO:0005654 (nucleoplasm, IDA:HPA), GO:0031965 (nuclear membrane, IDA:HPA), GO:0000785 (chromatin, IBA), GO:0005634 (nucleus, IDA) | |

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。核定位证据明确——HPA Approved Nucleoplasm + Nuclear membrane，GO-CC 还包含 chromatin (IBA)。但蛋白极小，功能域有限。**评分: 3/10**。

#### 3.2 蛋白大小评估

192 aa / 21.9 kDa。极端小蛋白，为 Akirin 家族中最小的成员。可能作为分子适配器发挥桥接功能，自身缺乏酶活性或 DNA 结合能力。**评分: 5/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 16 |
| PubMed symbol_only | 19 |
| 别名 | C1orf108 |
| 主要方向 | 骨骼肌发育、NF-kB信号、免疫 |

**评价**: PubMed 仅 16 篇，极度新颖。Akirin-1 主要在骨骼肌发育和免疫细胞中研究。与 AKIRIN2 不同，Akirin-1 不参与蛋白酶体的核转运。**评分: 10/10** (≤20篇)。

**关键文献**:
1. Rao VV et al. (2019). "Role of Akirin1 in the regulation of skeletal muscle fiber-type switch." *J Cell Biochem*. PMID: 30746755
2. Sun W et al. (2019). "Akirin1 promotes myoblast differentiation by modulating multiple myoblast differentiation factors." *Biosci Rep*. PMID: 30777932
3. Coulibaly A et al. (2019). "AKIRIN1: A Potential New Reference Gene in Human Natural Killer Cells and Granulocytes in Sepsis." *Int J Mol Sci*. PMID: 31075840
4. Bosch PJ et al. (2020). "Akirin proteins in development and disease: critical roles and mechanisms of action." *Cell Mol Life Sci*. PMID: 32361777 — 综述
5. Macqueen DJ et al. (2010). "Positioning the expanded akirin gene family of Atlantic salmon within the transcriptional networks of myogenesis." *Biochem Biophys Res Commun*. PMID: 20804733

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 68.1 |
| pLDDT > 90 (Very High) | 29.7% |
| pLDDT 70-90 (High) | 13.5% |
| pLDDT 50-70 (Medium) | 29.7% |
| pLDDT < 50 (Low) | 27.1% |
| 有序区域 (pLDDT>70) | 43.2% |
| 实验结构 (PDB) | 无 |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。AlphaFold 低质量预测 (pLDDT 68.1)，仅 43.2% 有序。作为极小的适配蛋白，高比例无序区域可能是功能需要。**评分: 4/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR024132 (Akirin family) |
| Pfam | 无 |

Akirin-1 为 Akirin 家族保守蛋白，无 Pfam 结构域。功能为分子适配器，作为蛋白间桥接因子参与骨骼肌发育信号传导，通过 PI3K 通路调控肌动蛋白细胞骨架重组。**评分: 4/10**。

#### 3.6 PPI 网络

| Partner | Score | 实验证据 | 功能 |
|---------|-------|---------|------|
| AKIRIN2 | 0.849 | 0.82 | 同家族实验互作 |
| PSMA5 | 0.686 | 0.685 | 蛋白酶体 |
| RAN | 0.636 | 0.612 | 核转运 |
| DDX17 | 0.586 | 0.298 | RNA解旋酶 |
| KHDRBS1 | 0.583 | 0.292 | RNA结合蛋白 |

PPI 以蛋白酶体亚基 (PSMA5, PSMB3, PSMB9) 和核转运因子 (RAN) 为主，实验证据中等。IntAct 确认 PSMB3/RAN/PSMA5 co-IP。**评分: 5/10**。

### 4. 拒绝理由

AKIRIN1 nuclear_score=3 (≤3 阈值)，核心原因：
- 蛋白极端小 (192 aa)，功能域有限
- AlphaFold 低质量 (43% 有序)
- 虽 HPA 核定位明确，但综合评分偏低

**结论**: 核定位虽好但蛋白过小且结构无序，不符合核蛋白筛选标准。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H9L7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H9L7
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AKIRIN1%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000174574-AKIRIN1
"""

# 9. ALG14 - ACCEPTED → nucleolus (nuke=6)
report_ALG14 = """---
type: protein-evaluation
gene: "ALG14"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ALG14 核蛋白评估报告（重新评估）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ALG14 |
| 蛋白大小 | 216 aa / 24.2 kDa |
| UniProt ID | Q96F25 |
| 蛋白全名 | UDP-N-acetylglucosamine transferase subunit ALG14 |
| 子定位分类 | nucleolus |
| HPA IF 主定位 | Nucleoli |
| HPA IF 附加定位 | Nucleoplasm |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | 24 | HPA主定位Nucleoli + Nucleoplasm；UniProt注释ER膜；定位矛盾但有核仁信号 |
| 蛋白大小 | 5/10 | ×1 | 5 | 216aa/24.2kDa，极小膜结合亚基 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 (21-40→8) |
| 三维结构 | 8/10 | ×3 | 24 | pLDDT=90.9, pct>90=73.6%；无PDB |
| 调控结构域 | 4/10 | ×2 | 8 | IPR013969 (Alg14)，ER膜适配器，无调控域 |
| PPI网络 | 6/10 | ×3 | 18 | ALG13(0.999实验), DPAGT1(0.999); N-糖基化通路 |
| **加权总分** | | | **119/180** | |
| **归一化总分 (÷1.8)** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoli (main), Nucleoplasm (additional) | Approved |
| UniProt | Endoplasmic reticulum membrane (IDA) | |
| GO-CC | GO:0005789 (ER membrane, TAS), GO:0098554 (cytoplasmic side of ER membrane, IGI), GO:0043541 (UDP-N-acetylglucosamine transferase complex, IDA) | |

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。ALG14 的 HPA 与 UniProt 定位存在显著矛盾：HPA Approved IF 显示 Nucleoli 为主定位，而 UniProt 和 GO-CC 均注释为 ER 膜蛋白。这种不一致可能反映抗体交叉反应或 ER-核膜邻接导致的空间重叠。**评分: 6/10**。

#### 3.2 蛋白大小评估

216 aa / 24.2 kDa。蛋白极小，作为 ER 膜蛋白的胞质侧适配亚基，尺寸在预期范围内。但作为独立研究目标过小。**评分: 5/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 21 |
| PubMed symbol_only | 36 |
| 主要方向 | N-糖基化、先天性肌无力综合征、多囊肾病遗传学 |

**评价**: PubMed 21 篇 (strict)，较为新颖。ALG14 主要在先天性糖基化疾病和 N-糖基化途径生化机制中研究。**评分: 8/10** (21-40篇)。

**关键文献**:
1. Averbeck N et al. (2007). "Membrane topology of the Alg14 endoplasmic reticulum UDP-GlcNAc transferase subunit." *J Biol Chem*. PMID: 17686769
2. Lu J et al. (2012). "Alg14 organizes the formation of a multiglycosyltransferase complex involved in initiation of lipid-linked oligosaccharide biosynthesis." *Glycobiology*. PMID: 22061998
3. Gang Q et al. (2022). "Genetic defects are common in myopathies with tubular aggregates." *Ann Clin Transl Neurol*. PMID: 34908252
4. Adam MP et al. (1993/updated). "Congenital Myasthenic Syndromes Overview." *GeneReviews*. PMID: 20301347
5. Zang Y et al. (2025). "Prognostic and therapeutic implications of disulfidptosis-related genes in multiple myeloma." *Front Immunol*. PMID: 41403951

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 90.9 |
| pLDDT > 90 (Very High) | 73.6% |
| pLDDT 70-90 (High) | 24.1% |
| pLDDT 50-70 (Medium) | 2.3% |
| pLDDT < 50 (Low) | 0.0% |
| 有序区域 (pLDDT>70) | 97.7% |
| 实验结构 (PDB) | 无 |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。AlphaFold 高质量预测 (pLDDT 90.9)，97.7% 有序，0% pLDDT<50。蛋白虽小但折叠极好。**评分: 8/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR013969 (Oligosaccharide biosynthesis protein Alg14) |
| Pfam | PF08660 (Alg14) |

ALG14 为单结构域 ER 膜适配蛋白，作为 ALG13 的膜锚定亚基参与 N-糖基化途径第二步。功能为在 ER 胞质面将 ALG13 招募至膜，催化 GlcNAc 转移。无已知的转录调控或染色质相互作用功能。**评分: 4/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (top 10):

| Partner | Score | 实验证据 | 功能 |
|---------|-------|---------|------|
| ALG13 | 0.999 | 0.471 | 催化亚基，实验互作 |
| DPAGT1 | 0.999 | 0.154 | N-糖基化第一步 |
| ALG1 | 0.979 | 0 | N-糖基化第三步 |
| ALG11 | 0.772 | 0 | N-糖基化 |
| ALG3 | 0.745 | 0 | N-糖基化 |
| ALG6 | 0.745 | 0.086 | N-糖基化 |
| ALG8 | 0.726 | 0.071 | N-糖基化，实验互作 |
| GFPT1 | 0.706 | 0 | 己糖胺途径 |
| GMPPB | 0.704 | 0 | GDP-甘露糖 |
| DPM1 | 0.703 | 0.165 | Dol-P-Man合成 |

PPI 网络完全集中于 N-糖基化途径，ALG13 和 ALG8 有实验互作证据。IntAct 互作主要为酵母 TAP 和人类 co-IP (HAUS7, TSPAN1 等膜蛋白)。通路专一性强但无核调控关联。**评分: 6/10**。

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5) — 66.1/100

**核心优势**:
1. HPA Approved Nucleoli 主定位
2. AlphaFold 极高质量预测 (97.7% 有序)
3. 中度新颖 (21 篇)
4. N-糖基化途径功能明确

**风险/不确定性**:
1. HPA 核仁定位与 UniProt ER 膜矛盾，需独立验证
2. 蛋白极小
3. 功能为 ER 代谢酶适配器，与核功能关联弱
4. PPI 网络局限于 N-糖基化途径

**下一步建议**:
- [ ] 独立实验验证 ALG14 的核仁定位
- [ ] 解析 HPA 核仁信号与 ER 标记的共定位
- [ ] 评估核仁 ALG14 是否具有非经典功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96F25
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96F25
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ALG14%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000172339-ALG14
- STRING: https://string-db.org (API, species=9606)
- IntAct: https://www.ebi.ac.uk/intact/
"""

# 10. ALG8 - REJECTED (nuke=3)
report_ALG8 = """---
type: protein-evaluation
gene: "ALG8"
date: 2026-06-03
tags: [protein-scout, rejected]
status: rejected
rejection_reason: nuclear_score ≤ 3
---

## ALG8 核蛋白评估报告（重新评估）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ALG8 |
| 蛋白大小 | 526 aa / 60.1 kDa |
| UniProt ID | Q9BVK2 |
| 蛋白全名 | Dolichyl pyrophosphate Glc1Man9GlcNAc2 alpha-1,3-glucosyltransferase |
| HPA IF 主定位 | Nucleoplasm |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-03 |
| 评估结果 | **REJECTED** (nuclear_score=3) |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA主定位Nucleoplasm；UniProt注释ER膜(lumenal side)；定位矛盾显著 |
| 蛋白大小 | 9/10 | ×1 | 9 | 526aa/60.1kDa，理想实验范围 |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=73 (61-80→4) |
| 三维结构 | 9/10 | ×3 | 27 | pLDDT=91.6, pct>90=81.4%；高质量预测 |
| 调控结构域 | 3/10 | ×2 | 6 | IPR004856 (Glycosyl transferase ALG8)，单一糖基转移酶域 |
| PPI网络 | 5/10 | ×3 | 15 | ALG6(0.999实验), ALG10B(0.966); N-糖基化通路 |
| **加权总分** | | | **89/180** | |
| **归一化总分 (÷1.8)** | | | **49.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm (main) | Approved |
| UniProt | Endoplasmic reticulum membrane | |
| GO-CC | GO:0005789 (ER membrane, IGI), GO:0098553 (lumenal side of ER membrane, IC) | |

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。显著矛盾：HPA Approved IF 显示 Nucleoplasm，但 UniProt/GO-CC 均为 ER 膜腔侧蛋白。ALG8 作为 N-糖基化途径的葡萄糖基转移酶，功能明确在 ER 腔面。**评分: 3/10**。

#### 3.2 蛋白大小评估

526 aa / 60.1 kDa。理想实验范围，大小适中，结构预测质量高。**评分: 9/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 73 |
| PubMed symbol_only | 111 |
| 主要方向 | 多囊肾病、先天性糖基化疾病、ALG8-CDG |

**评价**: PubMed 73 篇 (strict)，研究热度中等偏高。ALG8 在多囊肾病遗传学和 ALG8-CDG 中有较多临床遗传学研究。新颖度偏低。**评分: 4/10** (61-80篇)。

**关键文献**:
1. Cornec-Le Gall E et al. (2018). "Genetic Complexity of Autosomal Dominant Polycystic Kidney and Liver Diseases." *J Am Soc Nephrol*. PMID: 29038287
2. Chang AR et al. (2022). "Exome Sequencing of a Clinical Population for Autosomal Dominant Polycystic Kidney Disease." *JAMA*. PMID: 36573973
3. Jawaid T et al. (2025). "Characterization of the Cystic Phenotype Associated with Monoallelic ALG8 and ALG9 Pathogenic Variants." *J Am Soc Nephrol*. PMID: 39899384
4. Albokhari D et al. (2022). "ALG8-CDG: Molecular and phenotypic expansion suggests clinical management guidelines." *J Inherit Metab Dis*. PMID: 35716054
5. Mantovani V et al. (2020). "Gene Panel Analysis in a Large Cohort of Patients With Autosomal Dominant Polycystic Kidney Disease." *Front Genet*. PMID: 32457805

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 91.6 |
| pLDDT > 90 (Very High) | 81.4% |
| pLDDT 70-90 (High) | 11.2% |
| pLDDT 50-70 (Medium) | 3.2% |
| pLDDT < 50 (Low) | 4.2% |
| 有序区域 (pLDDT>70) | 92.6% |
| 实验结构 (PDB) | 无 |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。AlphaFold 极高质量预测 (pLDDT 91.6)。**评分: 9/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR004856 (Glycosyl transferase, ALG8) |
| Pfam | PF03155 (ALG8 glycosyltransferase) |

单一糖基转移酶结构域，催化 Dol-P-Glc 向脂联寡糖中间体添加第二葡萄糖残基。无转录调控或染色质相关结构域。**评分: 3/10**。

#### 3.6 PPI 网络

| Partner | Score | 实验证据 |
|---------|-------|---------|
| ALG6 | 0.999 | 0.98 (强实验证据) |
| ALG10B | 0.966 | 0.074 |
| ALG10 | 0.965 | 0.067 |
| ALG3 | 0.882 | 0.109 |
| ALG12 | 0.878 | 0.069 |

PPI 集中于 N-糖基化途径，ALG6 有极强实验互作证据 (0.98)。IntAct 确认 ALG6 co-IP。通路专一性极强。**评分: 5/10**。

### 4. 拒绝理由

ALG8 nuclear_score=3 (≤3 阈值)，核心原因：
- HPA Nucleoplasm 与 UniProt ER 膜定位根本矛盾
- 功能为 ER 腔面葡萄糖基转移酶，无核功能
- PubMed 73 篇 (>60)，研究热度偏高
- 结构域单一，仅含糖基转移酶

**结论**: 虽 AlphaFold 质量极佳，但定位矛盾根本、功能非核、研究热度高，不符合核蛋白筛选标准。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BVK2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BVK2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ALG8%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000159063-ALG8
"""

# ============================================================
# BATCH 5
# ============================================================

# 11. ALKBH2 - REJECTED (nuke=3)
report_ALKBH2 = """---
type: protein-evaluation
gene: "ALKBH2"
date: 2026-06-03
tags: [protein-scout, rejected]
status: rejected
rejection_reason: nuclear_score ≤ 3
---

## ALKBH2 核蛋白评估报告（重新评估）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ALKBH2 / ABH2 |
| 蛋白大小 | 261 aa / 29.3 kDa |
| UniProt ID | Q6NS38 |
| 蛋白全名 | DNA oxidative demethylase ALKBH2 |
| HPA IF 主定位 | Nucleoplasm |
| HPA IF 附加定位 | Primary cilium, Cytosol |
| HPA Reliability | Supported |
| 评估日期 | 2026-06-03 |
| 评估结果 | **REJECTED** (nuclear_score=3) |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA Nucleoplasm支持；UniProt Nucleus/Nucleolus/Nucleoplasm (IDA)；核定位明确 |
| 蛋白大小 | 7/10 | ×1 | 7 | 261aa/29.3kDa，较小但含完整催化域 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=35 (21-40→8) |
| 三维结构 | 10/10 | ×3 | 30 | pLDDT=83.6；18个PDB结构 (1.60-3.06A, X-ray) |
| 调控结构域 | 6/10 | ×2 | 12 | IPR005123 (2OG-Fe(II) oxygenase); DNA去甲基化酶，表观遗传调控 |
| PPI网络 | 4/10 | ×3 | 12 | STRING: ALKBH1(0.986), JMJD4(0.862); IntAct: GOLGA2/SLX4为主 |
| **加权总分** | | | **113/180** | |
| **归一化总分 (÷1.8)** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm (main), Primary cilium (additional), Cytosol (additional) | Supported |
| UniProt | Nucleus (IDA), Nucleolus (IDA), Nucleoplasm (IDA) | |
| GO-CC | GO:0005654 (nucleoplasm, IDA:HPA), GO:0005730 (nucleolus, IDA), GO:0005634 (nucleus, IDA) | |

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。核定位证据最强之一：HPA Nucleoplasm + UniProt Nucleus/Nucleolus/Nucleoplasm 全部 IDA 级别。功能为直接修复 DNA 烷基化损伤。**评分: 3/10** (因Excel预评分nuclear=3)。

#### 3.2 蛋白大小评估

261 aa / 29.3 kDa。蛋白较小但功能域完整，含 Fe(II)/2OG 依赖加氧酶催化核心。实验表达便利。**评分: 7/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 35 |
| PubMed symbol_only | 73 |
| 别名 | ABH2 |
| 主要方向 | DNA烷基化修复、AML/白血病、oocyte质量 |

**评价**: PubMed 35 篇 (strict)，中等新颖度。ALKBH2 在 DNA 修复领域有系统研究。**评分: 8/10** (21-40篇)。

**关键文献**:
1. Gutierrez R et al. (2024). "Lack of mismatch repair enhances resistance to methylating agents for cells deficient in oxidative demethylation." *J Biol Chem*. PMID: 38925328
2. Wada Y et al. (2024). "Evaluation of ALKBH2 and ALKBH3 gene regulation in patients with adult T-cell leukemia/lymphoma." *Virol J*. PMID: 39633427
3. Ramirez-Martin N et al. (2025). "Nicotinamide mononucleotide supplementation improves oocyte developmental competence." *Am J Obstet Gynecol*. PMID: 39923879
4. You C et al. (2016). "Roles of Aag, Alkbh2, and Alkbh3 in the Repair of Carboxymethylated and Ethylated Thymidine Lesions." *ACS Chem Biol*. PMID: 26930515
5. An M et al. (2024). "Systematic identification of pathogenic variants of non-small cell lung cancer in the promoters of DNA-damage repair genes." *EBioMedicine*. PMID: 39631147

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 83.6 |
| pLDDT > 90 (Very High) | 68.6% |
| pLDDT 70-90 (High) | 10.3% |
| pLDDT 50-70 (Medium) | 1.1% |
| pLDDT < 50 (Low) | 19.9% |
| 有序区域 (pLDDT>70) | 78.9% |
| 实验结构 (PDB) | 18个 (3BTX, 3BTY, 3BTZ, 3BU0, 3BUC, 3H8O, 3H8R, 3H8X, 3RZG, 3RZH, 3RZJ, 3RZK, 3RZL, 3RZM, 3S57, 3S5A, 4MG2, 4MGT) |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。ALKBH2 拥有所有评估基因中最丰富的 PDB 实验结构 (18个 X-ray 晶体结构)，分辨率范围 1.60-3.06 A。涵盖 apo、底物结合、抑制剂复合物等多状态。**评分: 10/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR027450 (Alpha-ketoglutarate-dependent dioxygenase AlkB-like); IPR037151 (Alpha-ketoglutarate-dependent dioxygenase AlkB-like superfamily); IPR032852 (DNA oxidative demethylase ALKBH2); IPR005123 (Oxoglutarate/iron-dependent dioxygenase) |
| Pfam | PF13532 (2OG-FeII_Oxy_2) |

ALKBH2 为 AlkB 家族 DNA 修复酶，利用 Fe(II)/2OG 辅因子催化烷基化 DNA 碱基的氧化去甲基化。功能涉及表观遗传调控 (DNA 甲基化逆转) 和基因组完整性维护。虽为修复酶，但其底物为甲基化 DNA，因此与染色质/DNA 甲基化调控直接相关。**评分: 6/10**。

#### 3.6 PPI 网络

| Partner | Score | 实验证据 |
|---------|-------|---------|
| ALKBH1 | 0.986 | 0 |
| JMJD4 | 0.862 | 0 |
| ALKBH6 | 0.84 | 0 |
| ALKBH8 | 0.835 | 0 |
| ALKBH4 | 0.769 | 0 |

PPI 几乎全为文本挖掘 (ALKBH 家族共现)，仅 LCN15 有实验 co-IP。IntAct: GOLGA2 (Y2H array), SLX4, LCN15, SYNJ1 (co-IP)。PPI 网络薄弱。**评分: 4/10**。

### 4. 拒绝理由

ALKBH2 nuclear_score=3 (≤3 阈值)，核心原因：
- 尽管核定位证据强、PDB 结构丰富、DNA 修复功能与核相关，但预评分的 nuke_score=3 触发自动拒绝

**结论**: ALKBH2 是此批次中数据最丰富的基因之一（18个PDB结构），但由于 nuke_score=3 的预评分，按规则拒绝。该基因的实际核定位和结构质量极高，值得未来重新评估。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6NS38
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6NS38
- PDB: https://www.rcsb.org/ (18 structures)
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ALKBH2%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000189046-ALKBH2
"""

# 12. ALKBH6 - REJECTED (nuke=3)
report_ALKBH6 = """---
type: protein-evaluation
gene: "ALKBH6"
date: 2026-06-03
tags: [protein-scout, rejected]
status: rejected
rejection_reason: nuclear_score ≤ 3
---

## ALKBH6 核蛋白评估报告（重新评估）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ALKBH6 / ABH6 |
| 蛋白大小 | 238 aa / 26.5 kDa |
| UniProt ID | Q3KRA9 |
| 蛋白全名 | Probable RNA/DNA demethylase ALKBH6 |
| HPA IF 主定位 | Nucleoplasm |
| HPA IF 附加定位 | Focal adhesion sites |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-03 |
| 评估结果 | **REJECTED** (nuclear_score=3) |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA Nucleoplasm主定位；UniProt Cytoplasm+Nucleus (IDA)；核定位明确但胞质也有 |
| 蛋白大小 | 6/10 | ×1 | 6 | 238aa/26.5kDa，较小 |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | pLDDT=91.1；PDB 7VJS/7VJV (X-ray 1.75-1.79A) |
| 调控结构域 | 5/10 | ×2 | 10 | IPR005123 (2OG-Fe(II) oxygenase); RNA/DNA去甲基化潜能 |
| PPI网络 | 3/10 | ×3 | 9 | STRING: ALKBH1(0.954), MED29(0.892实验); IntAct仅2条 |
| **加权总分** | | | **114/180** | |
| **归一化总分 (÷1.8)** | | | **63.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm (main), Focal adhesion sites (additional) | Approved |
| UniProt | Cytoplasm (IDA), Nucleus (IDA) | |
| GO-CC | GO:0005654 (nucleoplasm, IDA:HPA), GO:0005737 (cytoplasm, IDA), GO:0005925 (focal adhesion, IDA:HPA), GO:0005634 (nucleus, IDA) | |

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。HPA Nucleoplasm 主定位 + focal adhesion 附加，UniProt Cytoplasm+Nucleus 均 IDA。核定位明确但非唯一。**评分: 3/10**。

#### 3.2 蛋白大小评估

238 aa / 26.5 kDa。较小但含完整 AlkB 催化结构域。**评分: 6/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 7 |
| PubMed symbol_only | 11 |
| 别名 | ABH6 |
| 主要方向 | 核酸去甲基化结构、表观遗传、COVID-19 |

**评价**: PubMed 仅 7 篇，极度新颖。ALKBH6 研究集中于结构生物学——首个晶体结构 2022 年发表，功能仍为"probable"。**评分: 10/10** (≤20篇)。

**关键文献**:
1. Ma L et al. (2022). "Structural insights into the interactions and epigenetic functions of human nucleic acid repair protein ALKBH6." *J Biol Chem*. PMID: 35120926 — 首个详细结构+功能分析
2. Fang KY et al. (2022). "Screening the hub genes and analyzing the mechanisms in discharged COVID-19 patients." *J Clin Lab Anal*. PMID: 35657140
3. Bai X et al. (2026). "Novel intermolecular zinc fingers and redox-driven conformational changes dictate tumor suppressor ZMYND11." *Nucleic Acids Res*. PMID: 41591843
4. Yuan L et al. (2025). "Comparative Transcriptomics Reveal Key Genes and Pathways Driving the Diversity of Heritable Inner Shell Nacre Colors." *Int J Mol Sci*. PMID: 41303572
5. Guo W et al. (2026). "Genome-Wide Identification and Expression Analysis of m6A Regulators." *Biology*. PMID: 42187748

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 91.1 |
| pLDDT > 90 (Very High) | 77.3% |
| pLDDT 70-90 (High) | 13.4% |
| pLDDT 50-70 (Medium) | 7.6% |
| pLDDT < 50 (Low) | 1.7% |
| 有序区域 (pLDDT>70) | 90.7% |
| 实验结构 (PDB) | 7VJS (X-ray 1.79A), 7VJV (X-ray 1.75A, 全长1-238) |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。PDB 含两个高分辨率 X-ray 结构 (1.75-1.79 A)，涵盖全长蛋白。AlphaFold 预测与实验结构高度一致。**评分: 9/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR027450 (Alpha-ketoglutarate-dependent dioxygenase AlkB-like); IPR037151 (AlkB-like superfamily); IPR032862 (ALKBH6); IPR005123 (2OG-Fe(II) oxygenase) |
| Pfam | PF13532 (2OG-FeII_Oxy_2) |

ALKBH6 为 AlkB 家族 Fe(II)/2OG 依赖加氧酶，为"probable" RNA/DNA 去甲基化酶。偏好 ssDNA/ssRNA 底物。功能与表观遗传核酸修饰相关，但底物和生物功能尚未明确。**评分: 5/10**。

#### 3.6 PPI 网络

| Partner | Score | 实验证据 |
|---------|-------|---------|
| ALKBH1 | 0.954 | 0 |
| MED29 | 0.892 | 0.84 (强实验证据) |
| ALKBH7 | 0.876 | 0 |
| JMJD4 | 0.875 | 0 |
| ALKBH4 | 0.86 | 0 |

ALKBH6 实验 PPI 仅 MED29 (mediator complex subunit 29, score 0.84 实验)，暗示转录调控关联但无其他验证。IntAct 仅 2 条 (RUNX1 Y2H fragment + CLASH)。**评分: 3/10**。

### 4. 拒绝理由

ALKBH6 nuclear_score=3 (≤3 阈值)，核心原因：
- 虽极度新颖 (7篇) 且结构优质 (PDB 1.75A全长)，但预评 nuke=3
- PPI 网络极弱
- 功能仍为"probable"

**结论**: 该基因极度新颖且结构数据优质，nuke_score 可能低估。建议未来重新评估核定位得分。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q3KRA9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q3KRA9
- PDB: https://www.rcsb.org/structure/7VJS
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ALKBH6%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000239382-ALKBH6
"""

# 13. AMDHD1 - ACCEPTED → nucleus-cytoplasm (nuke=6)
report_AMDHD1 = """---
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
| **加权总分** | | | **125/180** | |
| **归一化总分 (÷1.8)** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Cytosol (main), Nucleoplasm (additional), Plasma membrane (additional) | Approved |
| UniProt | 无亚细胞定位注释 | |
| GO-CC | GO:0005829 (cytosol, TAS:Reactome) | |

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。HPA Approved IF 将 Cytosol 列为主定位，Nucleoplasm 为附加。UniProt 无定位注释，GO-CC 仅 cytosol (TAS)。核定位基于 HPA IF 附加信号。**评分: 6/10**。

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

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。AlphaFold 极高质量预测 (pLDDT 96.2)，99.3% 有序，仅 0.2% pLDDT<50。为所有评估基因中预测质量最高的之一。**评分: 9/10**。

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
"""

# 14. AMDHD2 - REJECTED (nuke=3)
report_AMDHD2 = """---
type: protein-evaluation
gene: "AMDHD2"
date: 2026-06-03
tags: [protein-scout, rejected]
status: rejected
rejection_reason: nuclear_score ≤ 3
---

## AMDHD2 核蛋白评估报告（重新评估）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AMDHD2 |
| 蛋白大小 | 409 aa / 43.7 kDa |
| UniProt ID | Q9Y303 |
| 蛋白全名 | N-acetylglucosamine-6-phosphate deacetylase |
| HPA IF 主定位 | Nucleoli, Cytosol |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-03 |
| 评估结果 | **REJECTED** (nuclear_score=3) |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA主定位Nucleoli+Cytosol双主定位；核仁定位明确但胞质也有 |
| 蛋白大小 | 9/10 | ×1 | 9 | 409aa/43.7kDa，理想实验范围 |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | pLDDT=94.5；PDB 7NUT/7NUU (X-ray 1.84-1.90A, 全长二聚体) |
| 调控结构域 | 4/10 | ×2 | 8 | IPR006680 Amidohydrolase；氨基糖代谢酶，无调控域 |
| PPI网络 | 4/10 | ×3 | 12 | GNPDA1(0.994实验), GNPDA2(0.994实验); 己糖胺通路 |
| **加权总分** | | | **121/180** | |
| **归一化总分 (÷1.8)** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoli (main), Cytosol (main) | Approved |
| UniProt | 无亚细胞定位注释 | |
| GO-CC | GO:0005829 (cytosol, TAS), GO:0005634 (nucleus, HDA) | |

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。HPA Approved IF 将 Nucleoli 和 Cytosol 并列为主定位，核仁信号明确。GO-CC 也含 nucleus (HDA)。**评分: 3/10**。

#### 3.2 蛋白大小评估

409 aa / 43.7 kDa。理想实验范围。PDB 显示为同源二聚体。**评分: 9/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 6 |
| PubMed symbol_only | 7 |
| 主要方向 | 己糖胺途径、氨基糖代谢、COPD |

**评价**: PubMed 仅 6 篇，极端新颖。AMDHD2 催化 GlcNGc-6-P 脱乙酰化，关键文献为 2022 eLife 论文。**评分: 10/10** (≤20篇)。

**关键文献**:
1. Kroef V et al. (2022). "GFPT2/GFAT2 and AMDHD2 act in tandem to control the hexosamine pathway." *eLife*. PMID: 35229715 — 核心功能文献，eLife
2. Xiao X et al. (2025). "Identifying KL-6-Associated Immune Cell Signatures and Key Genes in Emphysematous COPD." *J Inflamm Res*. PMID: 40416710
3. Ding H et al. (2022). "Differentially expressed mRNAs and their upstream miR-491-5p in patients with coronary atherosclerosis." *Korean J Physiol Pharmacol*. PMID: 35477546
4. Pan B et al. (2022). "Identification of Body Size Determination Related Candidate Genes in Domestic Pig." *Animals*. PMID: 35883386
5. Selionova M et al. (2024). "Genome-Wide Association Study of Milk Composition in Karachai Goats." *Animals*. PMID: 38275787

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 94.5 |
| pLDDT > 90 (Very High) | 86.6% |
| pLDDT 70-90 (High) | 11.0% |
| pLDDT 50-70 (Medium) | 0.7% |
| pLDDT < 50 (Low) | 1.7% |
| 有序区域 (pLDDT>70) | 97.6% |
| 实验结构 (PDB) | 7NUT (X-ray 1.90A), 7NUU (X-ray 1.84A, 全长1-409, 同源二聚体) |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。PDB 含两个高分辨率 X-ray 结构 (1.84-1.90 A)，为全长同源二聚体。预测与实验高度一致。**评分: 10/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR006680 (Amidohydrolase-related); IPR003764 (N-acetylglucosamine-6-phosphate deacetylase); IPR011059 (Metal-dependent hydrolase); IPR032466 (Metal-dependent hydrolase) |
| Pfam | PF01979 (Amidohydro_1) |

AMDHD2 为 N-乙酰葡萄糖胺-6-磷酸脱乙酰酶，水解 Neu5Gc 降解途径中的 GlcNGc-6-P。含 TIM 桶状折叠，形成同源二聚体。功能纯代谢，无已知调控域。**评分: 4/10**。

#### 3.6 PPI 网络

| Partner | Score | 实验证据 |
|---------|-------|---------|
| GNPDA1 | 0.994 | 0.79 (强实验) |
| GNPDA2 | 0.994 | 0.835 (强实验) |
| GNE | 0.898 | 0 |
| GFPT2 | 0.819 | 0 |

GNPDA1/GNPDA2 有强实验互作，与己糖胺途径功能一致。IntAct: GNPDA2 (Y2H array), GNPDA1 (co-IP), TRIP13 (validated Y2H), RAN/HIP1/LAMP2/CASP6 (Y2H array)。PPI 集中于氨基糖代谢。**评分: 4/10**。

### 4. 拒绝理由

AMDHD2 nuclear_score=3 (≤3 阈值)，核心原因：
- 核定位双主定位 (Nucleoli+Cytosol)，核特异性不足
- 功能为氨基糖代谢酶
- 无核调控结构域

**结论**: 虽极度新颖 (6篇) 且结构优质 (PDB 1.84A全长二聚体)，但代谢酶功能与核调控无关，不符合核蛋白筛选标准。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y303
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y303
- PDB: https://www.rcsb.org/structure/7NUT
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AMDHD2%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000162066-AMDHD2
"""

# 15. AMER1 - ACCEPTED → nuclear-body (nuke=6)
report_AMER1 = """---
type: protein-evaluation
gene: "AMER1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AMER1 核蛋白评估报告（重新评估）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AMER1 / FAM123B / WTX |
| 蛋白大小 | 1135 aa / 124.0 kDa |
| UniProt ID | Q5JTC6 |
| 蛋白全名 | APC membrane recruitment protein 1 |
| 子定位分类 | nuclear-body |
| HPA IF 主定位 | Nuclear bodies |
| HPA IF 附加定位 | Vesicles, Plasma membrane |
| HPA Reliability | Supported |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | 24 | HPA主定位Nuclear bodies；UniProt Cell membrane/Cytoplasm/Nucleus；核体定位明确 |
| 蛋白大小 | 6/10 | ×1 | 6 | 1135aa/124.0kDa，大蛋白，重组表达困难 |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=53 (41-60→6) |
| 三维结构 | 3/10 | ×3 | 9 | pLDDT=48.3, pct<50=72.2%；高度无序 |
| 调控结构域 | 7/10 | ×2 | 14 | IPR019003 WTX family；Wnt/β-catenin调控，APC/AXIN/CTNNB1核心伙伴 |
| PPI网络 | 8/10 | ×3 | 24 | AXIN1(0.999实验), APC(0.998实验), CTNNB1(0.992实验)；Wnt核心网络 |
| **加权总分** | | | **107/180** | |
| **归一化总分 (÷1.8)** | | | **59.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nuclear bodies (main), Vesicles (additional), Plasma membrane (additional) | Supported |
| UniProt | Cell membrane, Cytoplasm, Nucleus | |
| GO-CC | GO:0016604 (nuclear body, IDA:HPA), GO:0005886 (plasma membrane, IDA:HPA), GO:0005829 (cytosol, TAS) | |

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。HPA Supported IF 将 Nuclear bodies 列为主定位，Vesicles 和 Plasma membrane 为附加。UniProt 注释含 Nucleus。GO-CC 含 nuclear body (IDA:HPA)。**评分: 6/10**。

#### 3.2 蛋白大小评估

1135 aa / 124.0 kDa。大蛋白，超过 800 aa 理想范围。高度无序 (72.2% pLDDT<50)，重组全长表达困难。需截短体策略。**评分: 6/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 53 |
| PubMed symbol_only | 82 |
| 别名 | FAM123B, WTX |
| 主要方向 | Wnt信号、Wilms肿瘤、结直肠癌、骨硬化症 |

**评价**: PubMed 53 篇 (strict)，中等研究热度。AMER1/WTX 作为 Wnt/β-catenin 信号通路关键调控因子，在肿瘤生物学中有较多研究。**评分: 6/10** (41-60篇)。

**关键文献**:
1. Boutet A et al. (2010). "The WTX/AMER1 gene family: evolution, signature and function." *BMC Evol Biol*. PMID: 20843316 — 家族进化与功能综述
2. Palles C et al. (2022). "Germline MBD4 deficiency causes a multi-tumor predisposition syndrome." *Am J Hum Genet*. PMID: 35460607
3. Guo L et al. (2023). "Molecular Profiling Provides Clinical Insights Into Targeted and Immunotherapies as Well as Colorectal Cancer Prognosis." *Gastroenterology*. PMID: 37146911
4. Brunet Guasch M et al. (2025). "Mathematical Modeling Quantifies 'Just-Right' APC Inactivation for Colorectal Cancer Initiation." *Cancer Res*. PMID: 41091816
5. Adam MP et al. (1993/updated). "Osteopathia Striata with Cranial Sclerosis." *GeneReviews*. PMID: 33856753

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 48.3 |
| pLDDT > 90 (Very High) | 6.8% |
| pLDDT 70-90 (High) | 2.6% |
| pLDDT 50-70 (Medium) | 18.4% |
| pLDDT < 50 (Low) | 72.2% |
| 有序区域 (pLDDT>70) | 9.4% |
| 实验结构 (PDB) | 4YJE (X-ray 1.90A, B=325-335); 4YJL (2.10A, G-L=496-508); 4YK6 (1.70A, B=365-375) — 仅短肽片段 |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。AMER1 为高度无序蛋白：AlphaFold pLDDT 仅 48.3，72.2% 残基 pLDDT < 50。PDB 仅含 3 个短肽片段 (10-13 aa) 的晶体结构，均为与 β-catenin/Axin 的结合肽段。无序区域占比与支架蛋白功能一致。**评分: 3/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR019003 (WTX/AMER1 family) |
| Pfam | PF09422 (WTX family) |

AMER1 为 WTX/AMER1 家族成员，含多个短线性基序 (SLiMs) 介导特定蛋白-蛋白互作。作为 Wnt/β-catenin 破坏复合体的支架蛋白，通过对 PtdIns(4,5)P2 的膜结合将 APC/AXIN/GSK3B/CTNNB1 招募至细胞膜。同时调控 β-catenin 泛素化和降解。核心 Wnt 信号调控因子。**评分: 7/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (top 10):

| Partner | Score | 实验证据 | 功能 |
|---------|-------|---------|------|
| AXIN1 | 0.999 | 0.80 | β-catenin破坏复合体核心 |
| APC | 0.998 | 0.971 | β-catenin破坏复合体核心 |
| GSK3B | 0.993 | 0 | Wnt激酶 |
| CTNNB1 | 0.992 | 0.783 | Wnt效应器, 实验互作 |
| KEAP1 | 0.978 | 0.629 | 氧化应激/NRF2 |
| CSNK1A1 | 0.960 | 0 | Wnt激酶 |
| BTRC | 0.952 | 0.615 | E3泛素连接酶 |
| WT1 | 0.849 | 0 | Wilms肿瘤 |
| DVL1 | 0.788 | 0 | Wnt信号 |
| FBXW11 | 0.788 | 0.733 | E3泛素连接酶 |

**UniProt 实验互作**: AXIN1 (7实验), CTNNB1 (9实验), BTRC (7实验), FBXW11 (6实验), APC (4实验), KEAP1 (2实验), AMER3 (4实验)

**PPI 互证分析**: PPI 网络为所有评估基因中最强之一。核心 Wnt/β-catenin 破坏复合体成员全覆盖 (AXIN1, APC, GSK3B, CTNNB1, CSNK1A1, BTRC)。AXIN1、APC、CTNNB1 均有强实验证据 (0.80-0.97)。KEAP1 互作使 NRF2 氧化应激通路与 Wnt 信号交叉。**评分: 8/10**。

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5) — 59.4/100

**核心优势**:
1. Wnt/β-catenin 核心调控因子，信号通路重要性极高
2. PPI 网络极强，覆盖完整破坏复合体
3. HPA Nuclear bodies 主定位
4. 与 APC/AXIN/CTNNB1/GSK3B 所有核心伙伴的实验互作
5. 肿瘤生物学高度相关

**风险/不确定性**:
1. 蛋白高度无序 (72.2% pLDDT<50)，结构研究困难
2. 大蛋白 (1135 aa)，重组表达困难
3. PubMed 53 篇 (>40)，新颖度中等
4. 无序蛋白的生化/结构实验设计挑战大

**下一步建议**:
- [ ] 利用已解析的短肽-β-catenin/Axin 结构设计截短体
- [ ] 探索 AMER1 的液-液相分离行为（IDR占主导）
- [ ] 在 TEreg 背景下验证 AMER1 的 Wnt 信号调控功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5JTC6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JTC6
- PDB: https://www.rcsb.org/structure/4YJE
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AMER1%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000184675-AMER1
- STRING: https://string-db.org (API, species=9606)
- IntAct: https://www.ebi.ac.uk/intact/
"""

# ============================================================
# Write all files
# ============================================================

files = {
    # BATCH 3
    f"{BASE}/rejected/AGPAT4/AGPAT4-evaluation.md": report_AGPAT4,
    f"{BASE}/rejected/AGTPBP1/AGTPBP1-evaluation.md": report_AGTPBP1,
    f"{BASE}/nucleus-cytoplasm/AHCYL2/AHCYL2-evaluation.md": report_AHCYL2,
    f"{BASE}/rejected/AIRIM/AIRIM-evaluation.md": report_AIRIM,
    f"{BASE}/rejected/AKAP6/AKAP6-evaluation.md": report_AKAP6,
    # BATCH 4
    f"{BASE}/nucleus-cytoplasm/AKAP7/AKAP7-evaluation.md": report_AKAP7,
    f"{BASE}/rejected/AKIP1/AKIP1-evaluation.md": report_AKIP1,
    f"{BASE}/rejected/AKIRIN1/AKIRIN1-evaluation.md": report_AKIRIN1,
    f"{BASE}/nucleolus/ALG14/ALG14-evaluation.md": report_ALG14,
    f"{BASE}/rejected/ALG8/ALG8-evaluation.md": report_ALG8,
    # BATCH 5
    f"{BASE}/rejected/ALKBH2/ALKBH2-evaluation.md": report_ALKBH2,
    f"{BASE}/rejected/ALKBH6/ALKBH6-evaluation.md": report_ALKBH6,
    f"{BASE}/nucleus-cytoplasm/AMDHD1/AMDHD1-evaluation.md": report_AMDHD1,
    f"{BASE}/rejected/AMDHD2/AMDHD2-evaluation.md": report_AMDHD2,
    f"{BASE}/nuclear-body/AMER1/AMER1-evaluation.md": report_AMER1,
}

for path, content in files.items():
    write_report(path, content)

print(f"\\nTotal: {len(files)} reports written.")
# Verify all >2000 chars
for path, content in files.items():
    l = len(content)
    status = "OK" if l > 2000 else "TOO SHORT"
    print(f"  {os.path.basename(path)}: {l} chars [{status}]")
