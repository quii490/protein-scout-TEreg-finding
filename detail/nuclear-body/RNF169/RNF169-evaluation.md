---
type: protein-evaluation
gene: "RNF169"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## RNF169 (E3 ubiquitin-protein ligase RNF169) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | RNF169 |
| 蛋白全称 | E3 ubiquitin-protein ligase RNF169 |
| UniProt ID | Q8NCN4 |
| 蛋白大小 | 708 aa / 77.9 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 708 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR051657; InterPro:IPR001841; InterPro:IPR013083; InterPro:IPR017907; Pfam:PF13920 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Probable E3 ubiquitin-protein ligase that acts as a regulator of double-strand breaks (DSBs) repair following DNA damage. Functions in a non-canonical fashion to harness RNF168-mediated protein recruitment to DSB-containing chromatin, thereby contributing to regulation of DSB repair pathway utilization (PubMed:22492721, PubMed:30773093). Once recruited to DSB repair sites by recognizing and bindin

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR051657 |
| InterPro | IPR001841 |
| InterPro | IPR013083 |
| InterPro | IPR017907 |
| Pfam | PF13920 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000166439-RNF169
定位: location reactome" data-name="nucleoplasm,nuclear_bodies">

![](https://images.proteinatlas.org/38505/1806_D4_5_red_green.jpg)
![](https://images.proteinatlas.org/38505/1806_D4_9_red_green.jpg)
![](https://images.proteinatlas.org/38505/1898_E8_31_red_green.jpg)
![](https://images.proteinatlas.org/38505/1898_E8_32_red_green.jpg)
![](https://images.proteinatlas.org/38505/1840_A7_93_red_green.jpg)
![](https://images.proteinatlas.org/38505/1840_A7_95_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00184; |
| InterPro | IPR051657;IPR001841;IPR013083;IPR017907; |
| Pfam | PF13920; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| UBC | BioGRID | 0 |
| HIST2H2AC | BioGRID | 0 |
| HIST2H2BE | BioGRID | 0 |
| UBE2E1 | BioGRID | 0 |
| DYRK1B | BioGRID | 0 |
| DYRK1A | BioGRID | 0 |
| BRCA1 | BioGRID | 0 |
| HIST1H2BG | BioGRID | 0 |


### 深度机制分析

**结构域架构**：RNF169（708 aa，77.9 kDa）是DNA双链断裂（DSB）修复通路的关键E3泛素连接酶调控因子，结构域架构高度模块化：N端LRR结构域（约1-300 aa）——亮氨酸富集重复，预测采用马蹄形螺线管折叠（IPR051657），特异性识别RNF168催化的H2AK15ub和其他DSB位点泛素化产物；C端RING finger结构域（约550-600 aa, IPR001841, PF13920）——经典的C3HC4锌指RING结构域，配位两个Zn²⁺离子形成交叉支架（cross-brace）折叠，负责E3连接酶催化活性（Ub从E2转移至底物）；中央串联MIU（Motif Interacting with Ubiquitin, IPR017907）基序——识别K63连接泛素链，介导DSB位点泛素化信号的读取。AlphaFold pLDDT可用，RING结构域和LRR重复区预测质量中等。

**PPI互作网络解读**：PPI数据紧密聚焦于DSB修复的泛素化调控：UBC（泛素C，泛素前体）——泛素供体；HIST2H2AC/HIST2H2BE/HIST1H2BG——组蛋白H2A/H2B家族成员，RNF169的直接底物修饰靶标；UBE2E1——E2泛素结合酶，与RNF169的RING结构域互作并负责Ub递送；BRCA1——DNA损伤修复关键蛋白，RNF169通过竞争RNF168的泛素链结合位点调控BRCA1的DSB位点招募；DYRK1A/DYRK1B——双特异性酪氨酸磷酸化调控激酶，可能通过磷酸化RNF169调控其DSB修复活性（PMID:22492721, PMID:30773093）。

**结构解读**：RNF169通过一个精巧的"读取-调控-催化"三模块架构运作。LRR结构域的马蹄形内表面排列多个保守的疏水残基（Leu/Ile/Val），形成泛素化H2A的识别接口——特异性识别RNF168催化的H2AK15ub而非H2AK13ub（通过在LRR β-片层上表面的Arg口袋区分K15和K13的位置）。串联MIU基序形成"泛素链导向模块"——MIU1以高亲和力识别K63-Ub₂，MIU2提供额外的亲和力和选择性。RING结构域的交叉支架锌指折叠暴露Ub-结合E2（UBE2E1）的对接面——E2~Ub硫酯位于活性位点Cys上方，准备转移至底物Lys。

**机制模型**：（1）DSB发生后，ATM激酶磷酸化H2AX（γH2AX），招募MDC1-RNF8-RNF168泛素化级联；（2）RNF168催化H2AK15ub沉积——RNF169通过LRR结构域读取此信号并富集于DSB位点；（3）RNF169以非经典方式调控DSB修复通路选择：抑制53BP1（抗重组蛋白）的DSB招募，从而促进BRCA1介导的同源重组（HR）通路（而非NHEJ）——这是因为RNF169竞争性地结合了53BP1所需的H2AK15ub和K63-Ub链结合位点；（4）RNF169同时通过自身RING结构域催化额外的泛素化事件，进一步增强修复位点的泛素化信号，形成正反馈环；（5）DYRK1A/DYRK1B磷酸化调控RNF169的染色质亲和力和修复活性，连接了细胞周期调控和DNA修复。

**TE调控展望**：RNF169作为DSB修复调控因子，其TE调控关联在于以下几个方面：（1）ERV/LTR类TE的转录激活可产生R-loop结构（DNA:RNA杂交体+SSDNA），R-loop是DSB的来源之一，RNF169可能在TE来源的R-loop加工位点发挥修复通路选择作用；（2）H2AK15ub是异染色质区域（包括TE位点）的常见组蛋白修饰，RNF169可能通过与RNF168的功能拮抗调控特定TE区域的泛素化水平和染色质状态；（3）PMID:41145912揭示了H2BK120ub及其reader RNF169在复制叉重塑中的序列调控——复制叉在TE富集区域（如着丝粒周围异染色质）的停顿是已知现象，RNF169可能在这些区域保护停滞复制叉并促进HR介导的叉重启。

### PubMed 文献

**PubMed count: 34**

| 42314057 | PARG Governs a PARylation-Ubiquitination Toggle that Stabilizes RAD51AP1 to Drive Homologous Recombination-Mediated Chem | Cancer Res 2026 |
| 41145912 | H2BK120ub and its reader RNF169 sequentially regulate replication fork remodeling and stability. | EMBO J 2025 |
| 41107912 | miR-4793-3p predicts poor prognosis and regulates ferroptosis and invasiveness of breast cancer via targeting RNF169. | World J Surg Oncol 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/RNF169

