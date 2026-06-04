---
type: protein-evaluation
gene: "FGF3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FGF3 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=351，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FGF3 / INT2 |
| 蛋白名称 | Fibroblast growth factor 3 |
| 蛋白大小 | 239 aa / 26.9 kDa |
| UniProt ID | P11487 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Secreted |
| 蛋白大小 | 10/10 | ×1 | 10 | 239 aa / 26.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=351 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002209, IPR008996; Pfam: PF00167 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **63.0/180** | |
| **归一化总分** | | | **35.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Secreted | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- extracellular region (GO:0005576)
- extracellular space (GO:0005615)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 351 |
| PubMed broad count | 765 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: INT2 |

**关键文献**:
1. Molecular Characterization of KRAS Wild-type Tumors in Patients with Pancreatic Adenocarcinoma.. *Clinical cancer research : an official journal of the American Association for Cancer Research*. PMID: 35302596
2. scRNA-sequencing reveals subtype-specific transcriptomic perturbations in DRG neurons of Pirt(EGFPf) mice in neuropathic pain condition.. *eLife*. PMID: 36264609
3. Dissection of a CTCF topological boundary uncovers principles of enhancer-oncogene regulation.. *Molecular cell*. PMID: 38452764
4. Fgf9 promotes incisor dental epithelial stem cell survival and enamel formation.. *Stem cell research & therapy*. PMID: 39256850
5. Inactivation of Fgf3 and Fgf4 within the Fgf3/Fgf4/Fgf15 gene cluster reveals their redundant requirement for mouse inner ear induction and embryonic survival.. *Developmental dynamics : an official publication of the American Association of Anatomists*. PMID: 34719815

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.3 |
| 高置信度残基 (pLDDT>90) 占比 | 54.4% |
| 置信残基 (pLDDT 70-90) 占比 | 5.9% |
| 中等置信 (pLDDT 50-70) 占比 | 24.7% |
| 低置信 (pLDDT<50) 占比 | 15.1% |
| 有序区域 (pLDDT>70) 占比 | 60.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=78.3，有序区 60.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002209, IPR008996; Pfam: PF00167 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FGFR1 | 0.999 | 0.168 | — |
| FGFR2 | 0.999 | 0.447 | — |
| FGFR4 | 0.994 | 0.168 | — |
| KL | 0.991 | 0.045 | — |
| EGF | 0.988 | 0.053 | — |
| FGFR3 | 0.978 | 0.168 | — |
| FGFBP1 | 0.968 | 0.045 | — |
| HSPG2 | 0.946 | 0.051 | — |
| DCN | 0.936 | 0.000 | — |
| EGFR | 0.928 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=78.3 + PDB: 无 | pLDDT=78.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Secreted / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FGF3 — Fibroblast growth factor 3，研究基础较多，新颖性有限。
2. 蛋白大小239 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 351 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P11487
- Protein Atlas: https://www.proteinatlas.org/ENSG00000186895-FGF3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FGF3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P11487
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
