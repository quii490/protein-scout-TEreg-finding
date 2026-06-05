---
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

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

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

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

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

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000135049-AGTPBP1/subcellular

![](https://images.proteinatlas.org/71094/2124_E11_19_blue_red_green.jpg)
![](https://images.proteinatlas.org/71094/2124_E11_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/71094/2134_D10_12_blue_red_green.jpg)
![](https://images.proteinatlas.org/71094/2134_D10_51_blue_red_green.jpg)
![](https://images.proteinatlas.org/71094/2169_H5_20_blue_red_green.jpg)
![](https://images.proteinatlas.org/71094/2169_H5_37_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UPW5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
