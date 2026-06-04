---
type: protein-evaluation
gene: "BARD1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BARD1 — REJECTED (研究热度过高 (PubMed strict=562，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BARD1 |
| 蛋白名称 | BRCA1-associated RING domain protein 1 |
| 蛋白大小 | 777 aa / 86.6 kDa |
| UniProt ID | Q99728 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear speckles; 额外: Cytoplasmic bodies; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 777 aa / 86.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=562 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.2; PDB: 1JM7, 2NTE, 2R1Z, 3C5R, 3FA2, 6M14, 7E8I |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002110, IPR036770, IPR039503, IPR001357, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear speckles; 额外: Cytoplasmic bodies | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- BRCA1-A complex (GO:0070531)
- BRCA1-B complex (GO:0070532)
- BRCA1-BARD1 complex (GO:0031436)
- BRCA1-C complex (GO:0070533)
- cytoplasm (GO:0005737)
- cytoplasmic ribonucleoprotein granule (GO:0036464)
- nuclear speck (GO:0016607)
- nuclear ubiquitin ligase complex (GO:0000152)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 562 |
| PubMed broad count | 934 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Breast Cancer Risk Genes - Association Analysis in More than 113,000 Women.. *The New England journal of medicine*. PMID: 33471991
2. The antitumorigenic roles of BRCA1-BARD1 in DNA repair and replication.. *Nature reviews. Molecular cell biology*. PMID: 32094664
3. Germline Mutations in the BRIP1, BARD1, PALB2, and NBN Genes in Women With Ovarian Cancer.. *Journal of the National Cancer Institute*. PMID: 26315354
4. Promotion of DNA end resection by BRCA1-BARD1 in homologous recombination.. *Nature*. PMID: 39261729
5. Whole-exome Sequencing of Nigerian Prostate Tumors from the Prostate Cancer Transatlantic Consortium (CaPTC) Reveals DNA Repair Genes Associated with African Ancestry.. *Cancer research communications*. PMID: 36922933

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.2 |
| 高置信度残基 (pLDDT>90) 占比 | 27.7% |
| 置信残基 (pLDDT 70-90) 占比 | 24.5% |
| 中等置信 (pLDDT 50-70) 占比 | 6.4% |
| 低置信 (pLDDT<50) 占比 | 41.4% |
| 有序区域 (pLDDT>70) 占比 | 52.2% |
| 可用 PDB 条目 | 1JM7, 2NTE, 2R1Z, 3C5R, 3FA2, 6M14, 7E8I, 7JZV, 7LYB, 7LYC |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=64.2），有序残基占 52.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR039503, IPR001357, IPR036420; Pfam: PF12796, PF00533, PF14835 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UIMC1 | 0.999 | 0.477 | — |
| RAD51 | 0.999 | 0.758 | — |
| RBBP8 | 0.999 | 0.994 | — |
| BRCA2 | 0.999 | 0.793 | — |
| MRE11 | 0.999 | 0.994 | — |
| ABRAXAS1 | 0.999 | 0.994 | — |
| BRCA1 | 0.999 | 0.999 | — |
| BABAM2 | 0.999 | 0.334 | — |
| BRIP1 | 0.999 | 0.994 | — |
| BRCC3 | 0.999 | 0.647 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GIT1 | psi-mi:"MI:0096"(pull down) | pubmed:15383276|mint:MINT-5217 |
| KAT7 | psi-mi:"MI:0096"(pull down) | pubmed:15383276|mint:MINT-5217 |
| CEP126 | psi-mi:"MI:0096"(pull down) | pubmed:15383276|mint:MINT-5217 |
| TCERG1 | psi-mi:"MI:0096"(pull down) | pubmed:15383276|mint:MINT-5217 |
| CHD3 | psi-mi:"MI:0096"(pull down) | pubmed:15383276|mint:MINT-5217 |
| KAT5 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| ZHX1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| ELP1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| BRD7 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| KBTBD7 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.2 + PDB: 1JM7, 2NTE, 2R1Z, 3C5R, 3FA2,  | pLDDT=64.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nuclear speckles; 额外: Cytoplasmic bod | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BARD1 — BRCA1-associated RING domain protein 1，研究基础较多，新颖性有限。
2. 蛋白大小777 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 562 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=64.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 562 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99728
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138376-BARD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BARD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99728
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
