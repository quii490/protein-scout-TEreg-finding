---
type: protein-evaluation
gene: "LGSN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LGSN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LGSN / GLULD1, LGS |
| 蛋白名称 | Lengsin |
| 蛋白大小 | 509 aa / 57.3 kDa |
| UniProt ID | Q5TDP6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 509 aa / 57.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008147, IPR036651, IPR014746, IPR008146; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- membrane (GO:0016020)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GLULD1, LGS |

**关键文献**:
1. Targeting LGSN restores sensitivity to chemotherapy in gastric cancer stem cells by triggering pyroptosis.. *Cell death & disease*. PMID: 37612301
2. Trimetallic nanocomposites developed for efficient in vivo bimodal imaging via fluorescence and magnetic resonance.. *Journal of materials chemistry. B*. PMID: 39072712
3. Various cells retrovirally transduced with N-acetylgalactosoamine-6-sulfate sulfatase correct Morquio skin fibroblasts in vitro.. *Human gene therapy*. PMID: 11686941
4. Correction of the enzyme deficiency in hematopoietic cells of Gaucher patients using a clinically acceptable retroviral supernatant transduction protocol.. *Experimental hematology*. PMID: 8299741
5. Construction of retroviral vectors carrying human CD3 gamma cDNA and reconstitution of CD3 gamma expression and T cell receptor surface expression and function in a CD3 gamma-deficient mutant T cell line.. *Human gene therapy*. PMID: 9189762

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.5 |
| 高置信度残基 (pLDDT>90) 占比 | 53.0% |
| 置信残基 (pLDDT 70-90) 占比 | 16.3% |
| 中等置信 (pLDDT 50-70) 占比 | 12.8% |
| 低置信 (pLDDT<50) 占比 | 17.9% |
| 有序区域 (pLDDT>70) 占比 | 69.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=77.5，有序区 69.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008147, IPR036651, IPR014746, IPR008146; Pfam: PF00120 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GLUL | 0.940 | 0.000 | — |
| GMPS | 0.878 | 0.000 | — |
| TMEM109 | 0.859 | 0.000 | — |
| PC | 0.850 | 0.000 | — |
| IAH1 | 0.818 | 0.000 | — |
| GATB | 0.818 | 0.000 | — |
| NDUFS8 | 0.794 | 0.000 | — |
| FADS6 | 0.740 | 0.000 | — |
| FDXR | 0.738 | 0.000 | — |
| ATIC | 0.734 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=77.5 + PDB: 无 | pLDDT=77.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LGSN — Lengsin，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小509 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5TDP6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000146166-LGSN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LGSN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5TDP6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
