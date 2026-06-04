---
type: protein-evaluation
gene: "KRI1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KRI1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KRI1 |
| 蛋白名称 | Protein KRI1 homolog |
| 蛋白大小 | 703 aa / 82.6 kDa |
| UniProt ID | Q8N9T8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 703 aa / 82.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR018034, IPR024626; Pfam: PF05178, PF12936 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Enhanced |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 90S preribosome (GO:0030686)
- nucleolus (GO:0005730)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 26 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. H/ACA snR30 snoRNP guides independent 18S rRNA subdomain formation.. *Nature communications*. PMID: 40399280
2. A Novel Ferroptosis-Related Gene Signature to Predict Prognosis of Esophageal Carcinoma.. *Journal of oncology*. PMID: 35813863
3. Genome-wide profiling of a prognostic RNA-binding protein signature in esophageal cancer.. *Translational cancer research*. PMID: 40104740
4. Genome-wide association study of stage III/IV grade C periodontitis (former aggressive periodontitis) in a Spanish population.. *Journal of clinical periodontology*. PMID: 33745150
5. Yeast Krr1p physically and functionally interacts with a novel essential Kri1p, and both proteins are required for 40S ribosome biogenesis in the nucleolus.. *Molecular and cellular biology*. PMID: 11027267

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.4 |
| 高置信度残基 (pLDDT>90) 占比 | 17.4% |
| 置信残基 (pLDDT 70-90) 占比 | 44.2% |
| 中等置信 (pLDDT 50-70) 占比 | 11.5% |
| 低置信 (pLDDT<50) 占比 | 26.9% |
| 有序区域 (pLDDT>70) 占比 | 61.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=69.4），有序残基占 61.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018034, IPR024626; Pfam: PF05178, PF12936 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KRR1 | 0.996 | 0.902 | — |
| NOP14 | 0.944 | 0.125 | — |
| NOC2L | 0.931 | 0.000 | — |
| MPHOSPH10 | 0.928 | 0.419 | — |
| BMS1 | 0.921 | 0.000 | — |
| ESF1 | 0.920 | 0.000 | — |
| UTP23 | 0.896 | 0.260 | — |
| CEBPZ | 0.890 | 0.229 | — |
| UTP3 | 0.884 | 0.000 | — |
| POP1 | 0.877 | 0.843 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BEM2 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| BMS1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| BFR2 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| KRE33 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| KRR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| NOP14 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| PSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RPL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RPP0 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RPS0A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.4 + PDB: 无 | pLDDT=69.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KRI1 — Protein KRI1 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小703 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=69.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N9T8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000129347-KRI1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KRI1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N9T8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
