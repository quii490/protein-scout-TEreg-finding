---
type: protein-evaluation
gene: "ACSS2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ACSS2 — REJECTED (研究热度过高 (PubMed strict=205，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ACSS2 / ACAS2 |
| 蛋白名称 | Acetyl-coenzyme A synthetase, cytoplasmic |
| 蛋白大小 | 701 aa / 78.6 kDa |
| UniProt ID | Q9NR19 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles, Plasma membrane, Cytosol; UniProt: Cytoplasm, cytosol; Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 701 aa / 78.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=205 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011904, IPR032387, IPR025110, IPR045851, IPR020 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Plasma membrane, Cytosol | Supported |
| UniProt | Cytoplasm, cytosol; Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- mitochondrial matrix (GO:0005759)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 205 |
| PubMed broad count | 359 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ACAS2 |

**关键文献**:
1. ACSS2 acts as a lactyl-CoA synthetase and couples KAT2A to function as a lactyltransferase for histone lactylation and tumor immune evasion.. *Cell metabolism*. PMID: 39561764
2. Acetylation in the regulation of autophagy.. *Autophagy*. PMID: 35435793
3. Nucleus-Translocated ACSS2 Promotes Gene Transcription for Lysosomal Biogenesis and Autophagy.. *Molecular cell*. PMID: 28552616
4. ACSS2 protects against alcohol-induced hepatocyte ferroptosis through regulation of hepcidin expression.. *Nature communications*. PMID: 40593779
5. ACSS2 drives senescence-associated secretory phenotype by limiting purine biosynthesis through PAICS acetylation.. *Nature communications*. PMID: 40021646

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.4 |
| 高置信度残基 (pLDDT>90) 占比 | 71.2% |
| 置信残基 (pLDDT 70-90) 占比 | 19.0% |
| 中等置信 (pLDDT 50-70) 占比 | 5.4% |
| 低置信 (pLDDT<50) 占比 | 4.4% |
| 有序区域 (pLDDT>70) 占比 | 90.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.4，有序区 90.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011904, IPR032387, IPR025110, IPR045851, IPR020845; Pfam: PF16177, PF00501, PF13193 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CS | 0.983 | 0.070 | — |
| ACACA | 0.970 | 0.069 | — |
| ACACB | 0.960 | 0.069 | — |
| ACAT1 | 0.960 | 0.000 | — |
| ACOT12 | 0.959 | 0.000 | — |
| ACOX1 | 0.959 | 0.000 | — |
| ACAT2 | 0.959 | 0.000 | — |
| ACOX3 | 0.955 | 0.000 | — |
| ALDH2 | 0.954 | 0.060 | — |
| ACADS | 0.950 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.4 + PDB: 无 | pLDDT=89.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Cytoplasm; Nucleus / Nucleoplasm; 额外: Vesicles, Plasma membrane, Cytoso | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ACSS2 — Acetyl-coenzyme A synthetase, cytoplasmic，研究基础较多，新颖性有限。
2. 蛋白大小701 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 205 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 205 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NR19
- Protein Atlas: https://www.proteinatlas.org/ENSG00000131069-ACSS2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ACSS2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NR19
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000131069-ACSS2/subcellular

![](https://images.proteinatlas.org/70826/2265_A1_137_blue_red_green.jpg)
![](https://images.proteinatlas.org/70826/2265_A1_37_blue_red_green.jpg)
![](https://images.proteinatlas.org/4141/2060_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/4141/2060_G8_2_red_green.jpg)
![](https://images.proteinatlas.org/4141/78_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/4141/78_C8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NR19-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
