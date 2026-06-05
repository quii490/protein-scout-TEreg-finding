---
type: protein-evaluation
gene: "RHCE"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RHCE — REJECTED (研究热度过高 (PubMed strict=278，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RHCE / RHC, RHE |
| 蛋白名称 | Blood group Rh(CE) polypeptide |
| 蛋白大小 | 417 aa / 45.5 kDa |
| UniProt ID | P18577 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Plasma membrane; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 417 aa / 45.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=278 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=84.1; PDB: 7UZQ, 7V0K, 7V0S, 8CRT, 8CS9, 8CSL, 8CSX |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR029020, IPR024041, IPR002229; Pfam: PF00909 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.5/180** | |
| **归一化总分** | | | **46.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane | Uncertain |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- ankyrin-1 complex (GO:0170014)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 278 |
| PubMed broad count | 593 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RHC, RHE |

**关键文献**:
1. Architecture of the human erythrocyte ankyrin-1 complex.. *Nature structural & molecular biology*. PMID: 35835865
2. The RHCE gene encodes the chicken blood system I.. *Genetics, selection, evolution : GSE*. PMID: 38898419
3. Molecular genetics of RH.. *Vox sanguinis*. PMID: 10938938
4. Frequency and characterization of RHD and RHCE variants in the Noir Marron population from French Guiana.. *Transfusion*. PMID: 36286083
5. Variant genotypes associated with reduced expression of RhCE antigens among Brazilian blood donors.. *Transfusion*. PMID: 33687082

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.1 |
| 高置信度残基 (pLDDT>90) 占比 | 47.7% |
| 置信残基 (pLDDT 70-90) 占比 | 36.9% |
| 中等置信 (pLDDT 50-70) 占比 | 11.5% |
| 低置信 (pLDDT<50) 占比 | 3.8% |
| 有序区域 (pLDDT>70) 占比 | 84.6% |
| 可用 PDB 条目 | 7UZQ, 7V0K, 7V0S, 8CRT, 8CS9, 8CSL, 8CSX, 8CTE |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7UZQ, 7V0K, 7V0S, 8CRT, 8CS9, 8CSL, 8CSX, 8CTE）+ AlphaFold极高置信度预测（pLDDT=84.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029020, IPR024041, IPR002229; Pfam: PF00909 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RHAG | 0.992 | 0.900 | — |
| GYPB | 0.992 | 0.800 | — |
| GYPA | 0.975 | 0.900 | — |
| TMEM50A | 0.948 | 0.000 | — |
| CD47 | 0.932 | 0.000 | — |
| ANK1 | 0.927 | 0.900 | — |
| SLC4A1 | 0.880 | 0.800 | — |
| DHCR24 | 0.869 | 0.000 | — |
| EPB42 | 0.867 | 0.800 | — |
| PPP1R3A | 0.849 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=84.1 + PDB: 7UZQ, 7V0K, 7V0S, 8CRT, 8CS9,  | pLDDT=84.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. RHCE — Blood group Rh(CE) polypeptide，研究基础较多，新颖性有限。
2. 蛋白大小417 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 278 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 278 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P18577
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188672-RHCE/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RHCE
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P18577
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000188672-RHCE/subcellular

![](https://images.proteinatlas.org/60951/1443_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/60951/1443_C5_2_red_green.jpg)
![](https://images.proteinatlas.org/60951/1479_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/60951/1479_C5_2_red_green.jpg)
![](https://images.proteinatlas.org/60951/1825_G4_35_cr5ac33c563e019_red_green.jpg)
![](https://images.proteinatlas.org/60951/1825_G4_48_cr5ac33c563ef14_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P18577-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
