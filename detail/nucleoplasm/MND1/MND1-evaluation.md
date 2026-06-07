---
type: protein-evaluation
gene: "MND1"
date: 2026-01-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MND1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | MND1 |
| 别名 | GAJ |
| 基因全称 | meiotic nuclear divisions 1 |
| 蛋白名称 | Meiotic nuclear division protein 1 homolog |
| 蛋白大小 | 205 aa |
| UniProt ID | Q9BWT6 |
| 评估日期 | 2026-01-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| Nucleus 核定位特异性 | 8/10 | x4 | 32 | HPA: Nucleoplasm |
| Size 蛋白大小 | 10/10 | x1 | 10 | 205 aa |
| Novelty 研究新颖性 | 4/10 | x5 | 30 | PubMed: 63 篇 |
| 3D Structure 三维结构 | 8/10 | x3 | 24 | AlphaFold pLDDT=91.1 |
| Domain 调控结构域 | 7/10 | x2 | 14 | 无已注释染色质调控结构域 |
| PPI Network PPI网络 | 4/10 | x3 | 12 | STRING+IntAct+GO-CC |
| Cross-validation 互证加分 | — | max +3 | +0.5 | — |
|  | **原始总分** |  | **112.5/183** | **112.0/183** |  |  |  |
|  | **归一化总分** |  | **61.5/100** | **61.2/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

> **Protein Atlas IF**: 暂无HPA数据，核定位基于UniProt+GO

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA数据，核定位基于UniProt+GO | — |
| UniProt | Nucleus/DNA damage sites | — |
| GO-CC | GO:0005634 Nucleus (IEA) | — |

暂无 HPA IF 图片数据（Pending cell analysis），核定位基于 UniProt + GO 注释。


**结论**: 该蛋白在 HPA 中检测到Nucleoplasm信号，UniProt 注释为Nucleus/DNA damage sites。核定位得分 8/10。

#### 3.2 蛋白大小评估

205 aa，适合生化实验和结构解析

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 63 篇 |
| 最早发表年份 | 2026 |

**主要研究方向**:
- 功能研究尚不充分，属新颖蛋白

**关键文献**:
1. Peng JC et al. (2024). "Hop2-Mnd1 functions as a DNA sequence fidelity switch in Dmc1-mediated DNA recombination.". *Nat Commun*. PMID: 39463417
2. Tsubouchi H et al. (2023). "The Hop2-Mnd1 Complex and Its Regulation of Homologous Recombination.". *Biomolecules*. PMID: 37189409
3. Zelceski A et al. (2023). "MND1 and PSMC3IP control PARP inhibitor sensitivity in mitotic cells.". *Cell Rep*. PMID: 37163373
4. Lee W et al. (2023). "Hop2-Mnd1 and Swi5-Sfr1 stimulate Dmc1 filament assembly using distinct mechanisms.". *Nucleic Acids Res*. PMID: 37395447
5. Zhao Z et al. (2025). "MND1 Promotes the Proliferation of Prostate Cancer Cell Via the CCNB1/p53 Signaling Pathway.". *Curr Cancer Drug Targets*. PMID: 40353402


**评价**: PubMed 63 篇，属有一定研究基础蛋白，研究空间充足。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 91.1 |
| pLDDT > 90 占比 | 69.3% |
| pLDDT 70-90 占比 | 27.8% |
| pLDDT 50-70 占比 | 1.5% |
| pLDDT < 50 占比 | 1.5% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MND1/MND1-PAE.png]]

**评价**: AlphaFold 预测高质量，整体折叠良好 (AlphaFold v6, pLDDT=91.1, >90=69%, 70-90=28%, 50-70=2%, <50=2%)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | — |

**染色质调控潜力分析**: 无已注释染色质调控结构域

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-1554720|uniprotkb:A8MS27|uniprotkb:Q9SZE5 | MI:0007(anti tag coimmunoprecipitat | PMID:pubmed:17937504|imex:IM-19768 | — | — |
| intact:EBI-1100687|uniprotkb:Q3EAX3 | MI:0007(anti tag coimmunoprecipitat | PMID:pubmed:17937504|imex:IM-19768 | — | — |
| intact:EBI-307715|uniprotkb:Q4V3A9|uniprotkb:P93001|uniprotkb:Q9LIL0 | MI:0007(anti tag coimmunoprecipitat | PMID:pubmed:17937504|imex:IM-19768 | — | — |
| intact:EBI-307687 | MI:0007(anti tag coimmunoprecipitat | PMID:pubmed:17937504|imex:IM-19768 | — | — |
| intact:EBI-2270543|uniprotkb:Q9C7Y6|uniprotkb:Q9LQK4 | MI:0018(two hybrid) | PMID:pubmed:19187040|imex:IM-20264 | — | — |
|

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| PSMC3IP | 0.0 | — | — |
| RAD51 | 0.0 | — | — |
| EXO1 | 0.0 | — | — |
| BRCA2 | 0.0 | — | — |
| CHEK1 | 0.0 | — | — |
| RAD51AP1 | 0.0 | — | — |
| BRCA1 | 0.0 | — | — |
| MAD2L1 | 0.0 | — | — |
|

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 复合体注释


**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 15
- 仅 IntAct 实验: 9
- 调控相关比例: 2/15 (13%)

**评价**: PPI 得分 4/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=91.1, PDB=0 | — |
| 结构域 | UniProt/InterPro | 无注释域 | — |
| PPI | STRING + IntAct + GO-CC | 15/9/0 条目 | — |
| 定位 | HPA/UniProt/GO | Nucleoplasm / Nucleus / GO:0005634 | 一致 |

**互证加分明细**:
- IntAct+STRING 双源确认 (+0.5)
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ★★ (3/5)

**核心优势**:
1. 有一定研究基础 (PubMed 63 篇)，几乎未被研究
2. HPA 确认核定位，高置信度

**风险/不确定性**:
1. AlphaFold 结构预测置信度较高
2. PPI 数据丰富，功能网络尚不清晰

**下一步建议**:
- [ ] 通过 IF 实验验证内源核定位
- [ ] 构建表达载体进行功能研究
- [ ] Co-IP/MS 鉴定互作蛋白

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=MND1
- Protein Atlas: https://www.proteinatlas.org/MND1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MND1
- UniProt: https://www.uniprot.org/uniprotkb/Q9BWT6
- SMART: http://smart.embl.de/
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BWT6


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MND1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MND1/MND1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BWT6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR040661;IPR005647;IPR040453;IPR036390; |
| Pfam | PF18517;PF03962; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000121211-MND1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PSMC3IP | Intact, Biogrid, Opencell, Bioplex | true |
| BTF3L4 | Bioplex | false |
| CHMP1A | Bioplex | false |
| EIF1AX | Bioplex | false |
| EPS8 | Bioplex | false |
| HMGN1 | Bioplex | false |
| LETM1 | Bioplex | false |
| MAP1S | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
