---
type: protein-evaluation
gene: "EIF2B5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EIF2B5 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=131，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF2B5 |
| 蛋白名称 | Translation initiation factor eIF2B subunit epsilon |
| 蛋白大小 | 729 aa / 81.2 kDa |
| UniProt ID | A0A3B3IUB1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 729 aa / 81.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=131 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.9; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **61.5/180** | |
| **归一化总分** | | | **34.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Enhanced |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 131 |
| PubMed broad count | 134 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Infantile-Onset Vanishing White Matter Disease in an Azerbaijani Infant With a Homozygous EIF2B5 p.(Arg195His) Variant.. *Cureus*. PMID: 41727804
2. Adult-onset vanishing white matter disease caused by the EIF2B5 c.185A>T (p.Asp62Val) variant.. *Front Genet*. PMID: 41700296
3. Genetic Insights into Familial Hypospadias Identifying Rare Variants and Their Potential Role in Urethral Development.. *Genes (Basel)*. PMID: 41300791
4. Cell-specific Eif2b5 mutant mice: novel insights into roles of macroglia in vanishing white matter.. *Brain*. PMID: 40326783
5. Genetic variants in diminished ovarian reserve and premature ovarian insufficiency: implications for assisted reproductive outcomes.. *J Assist Reprod Genet*. PMID: 40936058

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.9 |
| 高置信度残基 (pLDDT>90) 占比 | 22.2% |
| 置信残基 (pLDDT 70-90) 占比 | 51.4% |
| 中等置信 (pLDDT 50-70) 占比 | 8.1% |
| 低置信 (pLDDT<50) 占比 | 18.2% |
| 有序区域 (pLDDT>70) 占比 | 73.6% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 中等质量（pLDDT=74.9，有序区 73.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF2B3 | 0.000 | 0.000 | — |
| EIF2B4 | 0.000 | 0.000 | — |
| EIF2B1 | 0.000 | 0.000 | — |
| EIF2B2 | 0.000 | 0.000 | — |
| EIF2S3 | 0.000 | 0.000 | — |
| EIF2S2 | 0.000 | 0.000 | — |
| EIF2S1 | 0.000 | 0.000 | — |
| RABIF | 0.000 | 0.000 | — |
| ARIH1 | 0.000 | 0.000 | — |
| EIF2S3B | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q13144 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P31232 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q5U3Y8 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q498U4 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q64350 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P49770 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:- |
| uniprotkb:Q14232 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:- |
| uniprotkb:P49841 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:- |
| uniprotkb:Q92837 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.9 + PDB: 无 | pLDDT=74.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EIF2B5 — Translation initiation factor eIF2B subunit epsilon，研究基础较多，新颖性有限。
2. 蛋白大小729 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 131 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A0A3B3IUB1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000145191-EIF2B5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF2B5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A3B3IUB1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
